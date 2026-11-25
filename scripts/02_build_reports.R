# Run this from the RStudio project root after 00_install_packages.R.
source('scripts/01_validate.R')
if (!requireNamespace('rmarkdown',quietly=TRUE)) {
  stop('RMarkdown is not installed. Run source("scripts/00_install_packages.R")')
}
rmarkdown::render('onderzoek.Rmd',output_file='onderzoek.html',envir=new.env(parent=globalenv()))
rmarkdown::render('product.Rmd',output_file='product.html',envir=new.env(parent=globalenv()))
message('Both HTML documents generated. Inspect product.html in your browser.')
