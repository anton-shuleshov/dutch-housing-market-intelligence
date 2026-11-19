# Download CBS StatLine datasets using the official OData API.
# Run from the RStudio project root with internet access.
# This script downloads raw CSVs; it does NOT assume they are cleaned.
#
# Install once: install.packages(c("readr", "jsonlite", "httr2"))
library(readr)
library(jsonlite)
library(httr2)

dir.create("data/raw/cbs", recursive = TRUE, showWarnings = FALSE)

tables <- c(
  sale_prices = "83625NED",
  housing_stock = "86286NED",
  household_income = "86380NED",
  house_price_index = "85773NED",
  rent_development = "83163NED",
  housing_construction = "82235NED",
  building_permits = "83671NED"
)

fetch_cbs <- function(table_id, filename) {
  # The legacy CBS API exposes TypedDataSet in pages.
  url <- paste0(
    "https://opendata.cbs.nl/ODataApi/OData/",
    table_id, "/TypedDataSet"
  )
  next_url <- paste0(url, "?%24top=10000")
  pages <- list()
  page <- 1L

  while (!is.null(next_url)) {
    message(table_id, ": downloading page ", page)
    response <- request(next_url) |>
      req_retry(max_tries = 3) |>
      req_perform()
    payload <- fromJSON(resp_body_string(response), flatten = TRUE)
    pages[[page]] <- as.data.frame(payload$value)
    next_url <- payload[["odata.nextLink"]]
    if (is.null(next_url)) {
      next_url <- payload[["__next"]]
    }
    if (!is.null(next_url) && !grepl("^https?://", next_url)) {
      next_url <- paste0(
        "https://opendata.cbs.nl", next_url
      )
    }
    page <- page + 1L
  }

  output <- do.call(rbind, pages)
  write_csv(output, filename)
  message("Saved ", nrow(output), " rows to ", filename)
  invisible(output)
}

for (name in names(tables)) {
  id <- tables[[name]]
  target <- file.path("data/raw/cbs", paste0(name, "_", id, ".csv"))
  tryCatch(
    fetch_cbs(id, target),
    error = function(e) message("FAILED ", id, ": ", conditionMessage(e))
  )
}

# IMPORTANT: CBS geographic and period codes require lookup tables
# before joining datasets. Validate the resulting raw CSVs.
