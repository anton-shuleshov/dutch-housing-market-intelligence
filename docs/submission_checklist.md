# Inholland — checklist voor eindoplevering (werkdocument)

## Vastgesteld via cursusvoorbeelden / besproken werkwijze
- [x] Onderzoek (exploratie) en presentatieproduct als afzonderlijke RMarkdown-bestanden voorbereid.
- [x] `product.Rmd` presenteert koppen, context, grafieken, discussie en bronnen.
- [x] Tabellen in HTML: `df_print: paged`.
- [x] Globaal `echo = FALSE`, `warning = FALSE`, `message = FALSE` voor het leesproduct (code staat wel in Rmd).
- [x] Alle datasetvelden, transformaties en aannames herleidbaar gemaakt.
- [x] Minimaal één analyse met verschillende perspectieven (woningprijs / inkomen / huurverdeling).
- [x] SQL en R tijdens de cursus besproken; het huidige product gebruikt R. SQL is niet gefingeerd als gebruikte techniek.

## Nog te controleren / afronden voor 11-12-2026
- [ ] Officiële opdrachttekst en beoordelingsrubric uit Moodle controleren (niet aanwezig onder onze gecontroleerde bronnen).
- [ ] Project ZIP uitpakken op Mac; `.Rproj` openen, packages installeren.
- [ ] `source('scripts/01_validate.R')` zonder fouten uitvoeren.
- [ ] `source('scripts/02_build_reports.R')` in een schone R-sessie uitvoeren.
- [ ] `product.html` in Safari controleren op leesbaarheid, assen, paginering en pagina-eindes.
- [ ] Interpretaties en belangrijke cijfers inhoudelijk zelf nalopen; taal en bronvermelding nakijken.
- [ ] Feedback van docent over gebruik van AI/tools en inlevervorm zo nodig verwerken.
- [ ] Verplichte bestandsnamen, uploadmogelijkheden en gewenste ZIP/HTML-begeleiding verifiëren.
- [ ] Kopie van definitieve versie lokaal én op GitHub veilig bewaren (geen persoonsgegevens of wachtwoorden uploaden).

## Wat is de minimale werkende set?
- `product.Rmd`, `onderzoek.Rmd`, `data/processed/*.csv`, `scripts/01_validate.R`, `scripts/02_build_reports.R`, `Dutch_Housing_Market_Intelligence.Rproj`.
- `product.html` en optioneel `onderzoek.html` ontstaan pas nadat RStudio Knit / render succesvol uitvoert. De huidige ZIP bevat de Rmd-bronnen en data, geen onbewezen geslaagde HTML-build.
