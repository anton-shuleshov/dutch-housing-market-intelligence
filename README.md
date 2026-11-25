# Dutch Housing Market Intelligence

**Woningprijzen, betaalbaarheid en sociale huur in Nederland**  
Anton Shuleshov • Inholland Academy / Big Data Business Analist  
Werkversie opgesteld op **25 november 2026** • geplande inlevering **11 december 2026**

Dit is een **reproduceerbaar RMarkdown-project**, geen mock-up. Gegevens uit zes echte CBS-ZIP's zijn gefilterd en gedocumenteerd; Woonservice-cijfers over 2025 zijn overgenomen uit de officiële regionale PDF (tabellen 4-2 en 4-3, p.24). Berekeningen in `product.Rmd` gebruiken de meegeleverde CSV's.

## Openen in RStudio op macOS

1. Pak de ZIP uit op je Mac (bij voorkeur in `Documents/Big_Data_Analytics/`).
2. Dubbelklik op `Dutch_Housing_Market_Intelligence.Rproj` om de juiste projectmap te openen.
3. Open RStudio **Console** en voer eenmalig uit: `source('scripts/00_install_packages.R')`.
4. Draai: `source('scripts/01_validate.R')`.
5. Draai: `source('scripts/02_build_reports.R')` of klik op **Knit** bij `product.Rmd`.
6. Open `product.html` in Safari. Controleer cijfers, grafieken en tekst; het HTML-bestand wordt bij jou lokaal gemaakt.

## Bestanden

| Pad | Inhoud |
|---|---|
| `onderzoek.Rmd` | Gedetailleerd analyse-notebook, kwaliteitscontroles, methodologische keuzes |
| `product.Rmd` | Gestileerd Nederlandstalig eindrapport met meerdere grafieken en conclusies |
| `scripts/prepare_cbs_zips.py` | Herhaalbare CBS ZIP → gelabelde CSV verwerkingscode (Python 3 standaardbibliotheek) |
| `scripts/00_install_packages.R` | Ontbrekende R-pakketten installeren |
| `scripts/01_validate.R` | Validatie van sleutels, dubbele data en regionale totalen |
| `scripts/02_build_reports.R` | Bouwt `onderzoek.html` en `product.html` met RMarkdown |
| `data/processed/` | Kleinschalige, direct te analyseren echte CBS-gegevens en Woonservice-data |
| `data/raw/cbs/` | Originele CBS bulk-ZIP's (in volledige lokale project-ZIP) |
| `data/raw/reports/` | Bron-PDF van Woonservice (in volledige lokale project-ZIP) |
| `data/raw/corporations/` | dVi2024-werkboek ter verkenning; nog niet geanalyseerd |
| `docs/methodology.md` | Gegevensdefinities, bronpagina's, caveats en ontbrekende bronnen |
| `docs/submission_checklist.md` | Eindcontrole en nog te verifiëren officiële eisen |

## Onderzoeksvraag
*Hoe ontwikkelen woningprijzen, betaalbaarheid en sociale huurtoewijzingen zich in Nederland en welke verschillen bestaan er tussen gemeenten?*

## Grenzen / wetenschappelijke eerlijkheid

- Gemeentelijke **gemiddelde** verkoopprijzen uit CBS 83625NED zijn niet hetzelfde als een prijsindex.
- Inkomen 2025 uit CBS 86380NED is **voorlopig**. Een woningprijs gedeeld door het mediane jaarinkomen is slechts een beschrijvende **proxy**.
- Woonservice IJmond/Zuid-Kennemerland heeft 7 gemeenten en **geen Uitgeest**.
- Statushouders, urgenten, loting en bemiddeling zijn niet altijd exclusieve categorieën.
- CBS `86286NED` is nog niet geleverd als bruikbare bron-ZIP; voorraadanalyse naar eigendom staat daarom niet in het huidige eindrapport.
- `dVi2024` is aanwezig als aanvullend bronbestand, maar nog niet inhoudelijk geanalyseerd.
- Aanvullende regels en beoordelingsrubric in Moodle moeten worden bevestigd. Het verslag wordt niet als ingeleverd of beoordeeld geclaimd.

**Databronnen:** [CBS](https://www.cbs.nl/), [Woonservice Trendmonitor](https://constaterendedat.nl/heemskerk/document/trendmonitor-woonruimteverdeling-ijmond-zuid-kennemerland-2025-93d1f8c3-c2a1-5417-b5ca-b4cd960d6ccb). Zie [methodologie](docs/methodology.md).
