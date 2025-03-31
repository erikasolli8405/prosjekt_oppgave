# Supportdata-analyse for MORSE

## Om prosjektet

Dette prosjektet utfører diverse analyser av supportdata fra telefonselskapet **MORSE**. Hver kundehenvendelse til MORSE blir loggført i en Excel-fil, og denne analysen fokuserer på data fra uke 24.

**Filnavn**: support_uke_24.xlsx

## Datastruktur

Filens kolonner er organisert som følger:

1.**Ukedag** - Dagen kunden tok kontakt

2.**Klokkeslett** - Tidspunkt for henvendelsen

3.**Varighet** - Lengden på samtalen i sekunder

4. **Kundetilfredshet** - Skala fra 1-10 (valgfri tilbakemelding)

## Analyser

Programmet utfører følgende analyser:

### Del A: Lese inn data

Lagrer data i fire arrays:

1. `u_dag`: Ukedager

2. `kl_slett`: Klokkeslett

3. `varighet`: Samtalevarigheter

4. `score`: Kundetilfredshet

### Del B: Antall henvendelser per ukedag

Teller antall henvendelser per ukedag og viser resultatet i et søylediagram.

### Del C: Minste og lengste samtaletid

Finnes og skrives ut med informativ tekst på hva var mist og lengs samtaletid i uke 24.

###Del D: Gjennomsnittlig samtaletid

Beregner gjennomsnittlig samtaletid for alle henvendelser i uke 24..

### Del E: Henvendelser per tidsbolk

Grupperer henvendelser i 2-timers intervaller:

-08-10

-10-12

-12-14

-14-16

Resultatet visualiseres med et sektordiagram.

### Del F: Beregning av Net Promoter Score (NPS)

Kundetilfredshet omgjøres til NPS basert på følgende regler:

-**1-6**: Negativ kunde

-**7-8**: Nøytral kunde

-**9-10**: Positiv kunde

NPS beregnes som:


## Bruk

1. Plasser `support_uke_24.xlsx` i samme mappe som Python-programmet.

2. Kjør programmet for å analysere dataene.

3. Se visualiseringene og analysene.

## Krav

- **Python 3**

### Biblioteker:

- `pandas` for databehandling

- `matplotlib` for visualisering

- `numpy` for beregninger
