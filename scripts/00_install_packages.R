# Run once in RStudio Console from the project root.
packages <- c('rmarkdown','knitr','dplyr','tidyr','readr','ggplot2','scales')
missing <- packages[!vapply(packages,requireNamespace,logical(1),quietly=TRUE)]
if (length(missing)) install.packages(missing,repos='https://cloud.r-project.org')
message('All required R packages installed or already present.')
