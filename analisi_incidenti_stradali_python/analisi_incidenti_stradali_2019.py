# Import delle librerie
import pandas as pd
import matplotlib.pyplot as plt
import pyfiglet
import os

# cli setup on windows shell
os.system("cls")
os.system("color 06")
os.system("title math analysis")

# Dichiarazione della lista delle opzioni (rimosso l'opzione 1)

opzioni = [
    "1. Incidenti stradali per tipo e comune - Anno 2019",
    "2. Incidenti stradali per regione - Anni 1986-2019",
    "3. Morti in incidente stradale nei Paesi europei - Anni 2010, 2015-2019",
    "4. Uscita dal programma"
]

# Titolo in ASCII art
text_title = pyfiglet.figlet_format("math-analysis", font="bubble")
print(text_title)

# Ciclo per caricare il menu
for opzione in opzioni:
    print(opzione)

# Main loop
while True:
    try:
        print("\nScegli tra le seguenti opzioni\n")
        scelta = int(input())

        while scelta <= 0 or scelta > 4:
            print("Errore: valore negativo o al di fuori delle opzioni\n")
            scelta = int(input())

        if scelta == 1:
            df = pd.read_excel("Incidenti stradali per tipo e comune - Anno 2019.xls", header=3, index_col=0)
            df = df.dropna()
            df = df.drop_duplicates()
            subset = df.iloc[0:18, 0:6]
            print(subset)
            subset.plot(kind='bar')
            plt.title("Incidenti stradali per tipo e comune - Anno 2019")
            plt.xlabel("Comuni in analisi")
            plt.show()

        elif scelta == 2:
            df = pd.read_excel("Incidenti stradali per regione - Anni 1986-2019.xls", header=2)
            df = df.dropna()
            df = df.drop_duplicates()
            subset = df.iloc[0:62, 0:13]
            print(subset)
            subset.plot(kind='line', x=subset.columns[0])
            plt.title("Incidenti stradali per regione - Anni 1986-2019")
            plt.show()

        elif scelta == 3:
            df = pd.read_excel("Morti in incidente stradale nei Paesi europei  - Anni 2010, 2015-2019.xls", header=2)
            df = df.dropna()
            df = df.drop_duplicates()
            subset = df.iloc[5:35, 0:6]
            print(subset)
            subset.plot(kind='bar', x=subset.columns[0])
            plt.xlabel("Stati membri del UE")
            plt.ylabel("Numero di morti")
            plt.title("Morti in incidenti stradali - UE (2010, 2015-2019)")
            plt.show()

        elif scelta == 4:
            print("Uscita dal software in corso...")
            break

    except (TypeError, ValueError):
        print("Errore: hai inserito un valore non valido")

    except KeyboardInterrupt:
        print("Errore nell'input da tastiera.")
