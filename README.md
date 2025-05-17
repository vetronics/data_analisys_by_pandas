
# Script di Analisi Dati Incidenti Stradali 🚗📊

---

## Descrizione 📝
Questo script Python è progettato per analizzare i dati sugli incidenti stradali utilizzando le librerie `pandas`, `matplotlib` e `pyfiglet`. Lo script offre diverse opzioni per caricare e visualizzare le statistiche sugli incidenti stradali, le morti e i feriti per diversi dataset e periodi di tempo. Una piccola porzione del dataset del **2019**, fornito dall'ACI (Automobile Club Italia) e dall'ISTAT (Istituto Nazionale di Statistica), è utilizzata per l'analisi in questo script.

Lo scopo principale dello script è fornire un'interfaccia a riga di comando (CLI) interattiva, dove l'utente può scegliere tra un insieme di opzioni predefinite per visualizzare i dati e generare visualizzazioni grafiche degli incidenti stradali, delle fatalità e delle lesioni.

---

## Funzionalità ⚙️
Lo script permette all'utente di scegliere tra le seguenti opzioni:

1. **Incidenti Stradali per Tipo e Comune - Anno 2019** 🚧🏙️
   - Mostra e visualizza gli incidenti stradali classificati per tipo e comune nel 2019.
   - I dati sono presentati sotto forma di un grafico a barre che mostra il numero di incidenti per comune.
   
2. **Incidenti Stradali per Regione - Anni 1986-2019** 🌍📈
   - Visualizza i dati sugli incidenti stradali aggregati per regione nel periodo 1986-2019.
   - I dati sono presentati sotto forma di un grafico a linee che mostra le tendenze degli incidenti per regione nel corso degli anni.

3. **Morti in Incidenti Stradali nei Paesi Europei - Anni 2010, 2015-2019** ⚰️🇪🇺
   - Mostra il numero di morti in incidenti stradali nei paesi dell'Unione Europea per gli anni 2010 e 2015-2019.
   - I dati sono presentati sotto forma di un grafico a barre che mostra il numero di morti per paese.

4. **Uscita dal Programma** 🚪
   - Esce dal programma.

---

## Requisiti 📋
Per eseguire lo script, è necessario avere le seguenti librerie Python installate:
- `pandas` per la manipolazione dei dati.
- `matplotlib` per la visualizzazione dei dati.
- `pyfiglet` per l'arte ASCII.
- `os` per l'interazione con il sistema (specifico per Windows per pulire la schermata e cambiare i colori).

Puoi installare le dipendenze necessarie utilizzando `pip`:

```bash
pip install pandas matplotlib pyfiglet


