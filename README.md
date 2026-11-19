# Dutch Housing Market Intelligence

**Housing Prices, Affordability, Social Housing & Market Dynamics in the Netherlands**

An R / RMarkdown research project exploring Dutch housing prices, income-based affordability, rental markets, social housing allocations, waiting times, construction and regional differences. The project is being developed for the **Inholland Academy Post-HBO Big Data Business Analist** course (target submission: **11 December 2026**) and a reproducible analytics portfolio.

## Research question

*Hoe ontwikkelen woningprijzen, betaalbaarheid, woningvoorraad en sociale huurtoewijzingen zich in Nederland, en welke verschillen bestaan er tussen gemeenten?*

The intended geographic scope is the Netherlands with a detailed focus on **Noord-Holland**. Municipal housing market indicators and region-specific social housing allocation statistics will be kept methodologically distinct.

## Current status

**Source discovery / research design.** A source register of 10 entries has been added. Five entries were labeled verified in an earlier review and five remain candidates; this does **not** mean all original files or table schemas have been independently downloaded and validated. **No analysis-ready datasets, finished figures or final results have been uploaded yet.**

## Repository contents

- [Source register](data/sources/source_register.csv) — source links, periods, status and caveats
- [Research plan](docs/research_plan.md) — research questions, scope, deliverables and validation checklist
- [Data dictionary](docs/data_dictionary.md) — proposed indicators and methodological cautions
- [Raw data directory](data/raw/README.md) — reserved for documented original data
- [Processed data directory](data/processed/README.md) — reserved for reproducible cleaned datasets

## Planned tools

R, RStudio, RMarkdown, dplyr, ggplot2 and official public statistics from CBS, Kadaster, DNB, housing corporations and regional allocation reports.

## Required Inholland outputs

`onderzoek.Rmd`, `product.Rmd`, `product.html`, and accompanying source data (or source references for large files), using relative paths and documented methodology.

## Data integrity

No synthetic housing observations are presented as actual results. Registration duration is not a guaranteed waiting time; corporation ownership is not equivalent to social-rent classification; allocation channels and recipient categories can overlap. All conclusions must be supported by cited datasets.

## Author

[Anton Shuleshov](https://github.com/anton-shuleshov)
