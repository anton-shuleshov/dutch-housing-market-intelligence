# Download and verification log

Date: 2026-11-19

## Successfully extracted source observations
- `data/verified/cbs_sale_prices_selected.csv`: 21 directly transcribed observations from the visible CBS 83625NED table (Haarlem, Utrecht and Arnhem; 2015 and 2020–2025).
- Source: https://www.cbs.nl/nl-nl/cijfers/detail/83625NED
- This is a **verified subset**, not the complete CBS dataset.
- Average sale price must not be treated as a constant-quality price index.

## Full raw files: not yet downloaded
The execution environment could not resolve `opendata.cbs.nl` for direct downloads. Consequently, **no full raw CSV, XLSX, ZIP or PDF is claimed to have been obtained**.

The script `scripts/download_cbs.R` is a reproducible downloader template to run in RStudio with internet access. Its behavior and output have **not** been execution-tested in this environment. Check CBS OData paging, table schemas, geographic code lookups and actual rows before analysis.

## Other sources pending
- Woonservice Trendmonitor: extract report tables with page references.
- Corporation dVi: download XLSX and inspect sheets.
- DNB: identify downloadable mortgage rate series.
- Uitgeest allocation region: obtain corresponding reports.

No invented data should be introduced to fill gaps.
