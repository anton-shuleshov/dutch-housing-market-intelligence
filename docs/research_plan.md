# Research plan — Dutch Housing Market Intelligence

**Course:** Inholland Academy, Post-HBO Big Data Business Analist (R / RMarkdown). **Submission target:** 11 December 2026.

## Research question
Hoe ontwikkelen woningprijzen, betaalbaarheid, woningvoorraad en sociale huurtoewijzingen zich in Nederland, en welke verschillen bestaan er tussen gemeenten?

## Scope
- National long-term housing market context, with a North Holland municipal comparison.
- Prices, real price trends, household income, rental market, housing stock, construction and demolition.
- Social housing allocation channels (loting, inschrijfduur, urgentie, directe bemiddeling), status holders and household categories where comparable aggregate statistics exist.
- Housing corporation sales and mortgage scenarios where supported by available data.

## Analysis principles
1. Separate national statistics from regional allocation systems; do not treat them as directly comparable without harmonized definitions.
2. Average transaction price is not a constant-quality house price index.
3. Corporation-owned stock is not equivalent to the number of regulated social rental homes.
4. Inschrijfduur at allocation is not the predicted waiting time of a newly registered applicant; zoekduur and slaagkans are different.
5. Statushouder is a recipient characteristic; directe bemiddeling is an allocation mechanism. Categories may overlap.
6. Permits are not completed homes; mortgage simulations are not lending eligibility.
7. Document year, geography, units, data vintage and source for each figure.
8. Use aggregate public data only; avoid identifiable personal records.
9. Interpret associations without claiming causation.

## Deliverables
- `onderzoek.Rmd`: exploration, cleaning, failed attempts and decisions.
- `product.Rmd`: polished Dutch-language analysis, readable code and visualizations.
- `product.html`: knitted report.
- Local data files or citations/links for files too large to submit.
- Reproducible relative paths, README and data dictionary.

## Next data-validation tasks
- Verify CBS table schemas, geographic keys, units, downloadability and actual observation periods.
- Download raw datasets; record URLs, access dates and licenses.
- Inspect Woonservice report tables and extract with exact page/table citations.
- Inspect dVi XLSX sheets and confirm availability of sales-to-tenants data.
- Find Uitgeest's relevant housing-allocation region and compatible reports.
- Determine a small common set of municipalities and years for reproducible charts.

**Status:** research design and source inventory only. No analysis-ready raw datasets are claimed.
