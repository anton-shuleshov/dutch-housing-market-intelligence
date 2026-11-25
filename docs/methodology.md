# Methodologie en bronregister (25 november 2026)

## Kernvraag
Hoe ontwikkelen woningprijzen, prijs-inkomensverhoudingen en sociale huurtoewijzingen zich in Nederland, en welke regionale verschillen zijn er?

## Direct gebruikte bronbestanden

| Dataset | Snapshot aanwezig | Variabele en selectie | Definitie / caveat |
|---|---|---|---|
| CBS 83625NED | ZIP 17-02-2026 | Gemiddelde verkoopprijs (M001534), regio + jaar 2015–2025 | Gemiddelde van verkochte woningen, niet constante-kwaliteit index |
| CBS 86380NED | ZIP 27-10-2026 | Populatie 1050010; kenmerken 1050010; mediaan besteedbaar inkomen M000933, x €1.000 | Alle particuliere huishoudens incl. studenten; 2025 *voorlopig*; regio-indeling 2026 |
| CBS 85773NED | ZIP 22-10-2026 | Nationale maandindex M001505_2, 2020=100 | Index is nationaal, niet per gemeente |
| CBS 82235NED | ZIP 20-03-2026 | Nieuwbouw M003003 en Sloop D003024 | Nationaal, BAG-methodiek; niet vergunningen |
| CBS 83163NED | ZIP 04-09-2026 | Huurverhoging D001503/D001504, totaal huurvormen | % jaarlijkse huurwijziging, geen huurprijsniveau |
| CBS 83671NED | ZIP 19-11-2026 | Woningen met verleende bouwvergunning A007233, T001209 + T001258, kwartaal | Gebouwvergunningen geen opgeleverde woningen |
| Woonservice Trendmonitor 2025 | PDF, 13-05-2026 | Tabellen 2-1, 4-2 en 4-3, pp. 10, 24 | IJmond/Zuid-Kennemerland, zeven gemeenten; Uitgeest uitgesloten |

Links: https://www.cbs.nl/nl-nl/cijfers/detail/83625NED ; https://www.cbs.nl/nl-nl/cijfers/detail/86380NED ; https://www.cbs.nl/nl-nl/cijfers/detail/85773NED ; https://www.cbs.nl/nl-nl/cijfers/detail/82235NED ; https://www.cbs.nl/nl-nl/cijfers/detail/83163NED ; https://www.cbs.nl/nl-nl/cijfers/detail/83671NED ; https://constaterendedat.nl/heemskerk/document/trendmonitor-woonruimteverdeling-ijmond-zuid-kennemerland-2025-93d1f8c3-c2a1-5417-b5ca-b4cd960d6ccb

## Techniek
De ZIP's gebruiken een long-format `Observations.csv`, met veldcodes. `prepare_cbs_zips.py` gebruikt `MeasureCodes.csv`, `RegioSCodes.csv` en `PeriodenCodes.csv` om de exacte betekenis te behouden. Het jaar wordt uit `YYYYJJ00` gehaald. `Utrecht (gemeente)` wordt tot `Utrecht` genormaliseerd (maar de CBS-regiocode GM0344 blijft de sleutel). Bedragen met decimale komma worden expliciet geconverteerd.

De prijs-inkomensratio = **gemeentelijke gemiddelde verkoopprijs / mediaan jaarlijks besteedbaar inkomen van huishoudens in die gemeente**. We voegen uitsluitend dezelfde regiocode en hetzelfde jaar samen. Een ratio van 10 wil NIET zeggen dat het huishouden een hypotheek ter waarde van tien jaarsalarissen kan krijgen. Evenmin bewijst deze vergelijking een causaal verband of meet zij de betaalbaarheid voor starters.

## Woonservice invoercontrole
De handmatig overgenomen tabel `woonservice_allocations_2025.csv` is afkomstig van **tabel 4-2 en tabel 4-3 op PDF-pagina 24**.

- Gemeenten: Beverwijk 416; Bloemendaal 56; Haarlem 966; Heemskerk 361; Heemstede 98; Velsen 592; Zandvoort 177.
- 2025 totaal 2.666 verhuringen: aanbodmodel 2.033; bemiddeling 633.
- Urgentie via aanbodmodel 164; via bemiddeling 382; urgentietotaal 546.
- COA/statushouders via bemiddeling 215 (onderdeel van bemiddeling; niet optellen bij totaal).
- Tabel 2-1 op p. 10 geeft regionale verhuurtotalen 2021=2.923, 2022=3.104, 2023=2.531, 2024=2.975, 2025=2.666.

**Let op:** Woonopmaat sluit vanaf juni 2023 aan op Woonservice. De administratieve reikwijdte wijzigt; dit kan trendvergelijkingen beïnvloeden. `Inschrijfduur`, `zoekduur` en `slaagkans` betekenen niet hetzelfde. `Statushouder` is een ontvangerscategorie; `directe bemiddeling` een toewijzingsmechanisme. Deze groepen kunnen overlappen.

## Niet geclaimd / vervolg
- CBS 86286NED (woningvoorraad eigendom) is nog niet bij de bron-ZIP's geleverd. Geen huur-/eigendomsvoorraadcijfers verzinnen.
- `dVi2024_H1-H5.xlsx` is lokaal bewaard, maar de tabellen/definities zijn nog niet gecontroleerd. Er worden geen cijfers over verkoop aan huurders aan ontleend.
- Nog geen gevalideerde hypotheekrenteserie, regionale wachttijddata Uitgeest of huurprijsniveaus (€/maand).
- De officiële beoordelingsrubric voor Inholland is nog niet als controleerbare bron beschikbaar. De rapportstructuur is gebaseerd op voorbeelden/schermafbeeldingen, niet op een vastgestelde eis voor aantal figuren.

## Reproduceerbaarheid
Zet zes CBS-ZIP's onder `data/raw/cbs/` en draai `python3 scripts/prepare_cbs_zips.py` om de CBS-data te vernieuwen. De Woonservice-CSV is met bronpagina apart vastgelegd. In RStudio: `source('scripts/00_install_packages.R')` eenmalig, dan `source('scripts/02_build_reports.R')`. Eerst `01_validate.R` uitvoeren vóór `rmarkdown::render()`.
