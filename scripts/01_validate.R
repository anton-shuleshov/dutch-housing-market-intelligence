# Validate source tables and key relationships before building the report.
library(readr)
library(dplyr)
load_csv <- function(name) {
  p <- file.path('data','processed',name)
  stopifnot(file.exists(p))
  read_csv(p,show_col_types=FALSE)
}
prices <- load_csv('cbs_municipal_sale_prices.csv')
income <- load_csv('cbs_municipal_income.csv')
aff <- load_csv('cbs_price_to_income_ratio.csv')
alloc <- load_csv('woonservice_allocations_2025.csv')

stopifnot(nrow(prices)>100, nrow(income)>200, nrow(aff)>100,
          !anyDuplicated(prices[c('year','region_code')]),
          !anyDuplicated(income[c('year','region_code','income_measure')]),
          !anyDuplicated(aff[c('year','region_code')]),
          all(is.finite(aff$price_to_income_ratio)),
          all(aff$price_to_income_ratio>0),
          all(alloc$offer_model+alloc$direct_mediation==alloc$total_allocations),
          all(alloc$urgency_offer_model+alloc$urgency_mediation==alloc$urgency_total),
          sum(alloc$total_allocations)==2666,
          sum(alloc$urgency_total)==546,
          sum(alloc$statusholders_via_mediation)==215)

message('VALIDATION PASSED: ',nrow(prices),' municipal price points; ',
        nrow(aff),' price-income ratios; ',sum(alloc$total_allocations),' social allocations.')
message('CAUTION: 2025 household income is voorlopige CBS data. Housing stock table 86286NED missing.')
