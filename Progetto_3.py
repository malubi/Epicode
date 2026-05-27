print("="*40, "Progetto 3", "="*40)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Parte 1- Variabili e tipi di dati
nome_cliente = "Gianni"
cognome_cliente = "Morandi"
età_cliente = 30
saldo_conto = 17520.47
cliente_vip = True
destinazioni_possibili = ["Roma", "Parigi", "Londra", "New York", "Tokyo"]
prezzo_destinazione = {"Roma": 25, "Parigi": 70, "Londra": 150, "New York": 175, "Tokyo": 120}
                      
#Parte2 - Programmazione ad oggetti
class Cliente:
    def __init__(self, nome, cognome, età, cliente_vip):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.cliente_vip = cliente_vip

    def visualizza_informazioni(self):
        print("\nInformazioni del cliente:")
        print(f"\nNome: {self.nome} {self.cognome}")
        print(f"\nEtà: {self.età}")
        print(f"Cliente VIP: {self.cliente_vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
    
    def importo_finale(self):
        if self.cliente.cliente_vip:
            prezzo_viaggio = 0.9*self.viaggio.prezzo
        else:
            prezzo_viaggio = self.viaggio.prezzo
        return prezzo_viaggio
    
    def dettagli(self):
        print(f"\nIl prezzo del viaggio a {self.viaggio.destinazione} di {self.cliente.nome} {self.cliente.cognome} è di {self.importo_finale()}€")
    
c1 = Cliente("Gianna", "Nannini", 52, True)
v1 = Viaggio("Tokyo", 1700, 15)
p1 = Prenotazione(c1, v1)

print("\n--parte 2 --")
p1.dettagli()

#Parte 3 -Numpy
prenotazioni = np.random.randint(200, 2000, size = 100)

prezzo_medio = np.mean(prenotazioni)
prezzo_minimo = np.min(prenotazioni)
prezzo_massimo = np.max(prenotazioni)
dev_stand_prezzo = np.std(prenotazioni)

prenotazioni_migliori = prenotazioni > prezzo_medio

prenotazioni_migliori_tot = np.sum(prenotazioni_migliori)
print("\n--PARTE 3 --")
print(f"\nLe prenotazioni sopra la media sono il {(prenotazioni_migliori_tot/len(prenotazioni))*100} %")

#Parte 4 - Pandas
#Imposto il seed per avere sempre gli stessi numeri generati casualmente
np.random.seed(42)

#Considero dei clienti generici che genero in modo random
clienti = [f"Cliente_{i}" for i in range(1, 21)]

#Prendo le destinazioni definite nel dizionario della parte 1 e le trasformo in una lsita
destinazioni_base = list(prezzo_destinazione.keys())

#Creo un array con le destinazioni della lista precedente inserite casualmente
destinazioni_casuali = np.random.choice(destinazioni_base, size = 20)

durata = np.random.randint(7, 20, size = 20)

giorno_partenza = np.random.randint(1, 31, size = 20)

dati_agenzia = pd.DataFrame({
    "Clienti" : clienti,
    "Destinazioni" : destinazioni_casuali,
    "Durata" : durata,
    "Giorno partenza (Luglio 2026)": giorno_partenza,
})

#Collego il prezzo della destinazione alla destinazione facendo riferimento al dizionario definito nella parte 1
dati_agenzia["Prezzo"] = dati_agenzia["Destinazioni"].map(prezzo_destinazione)

#Moltiplico il prezzo giornaliero della destinazione con la durata del viaggio per ottenere l'incasso
dati_agenzia["Incasso"] = dati_agenzia["Prezzo"] * dati_agenzia["Durata"]

print("\n-- parte 4 --")
print("\nSCHEDA VIAGGI")
print(dati_agenzia)

#Calcolo con Pandas l'incasso totale, medio per destinazione e top 3 destinazioni più vendute
incasso_totale = dati_agenzia["Incasso"].sum()
incasso_medio_per_destinazione = dati_agenzia.groupby("Destinazioni")["Incasso"].mean()
destinazioni_più_vendute = dati_agenzia["Destinazioni"].value_counts().head(3)


print("\nStatistica vendite:")
print("\nL'incasso totale dell'agenzia è: ", incasso_totale, "€")
print("\nL'incasso medio di ogni destinazione è:\n", incasso_medio_per_destinazione)
print("\nLe destinzioni più vendute sono:\n", destinazioni_più_vendute)

#Parte 5 - Matplotlib
plt.figure(figsize = (8, 5))
#per fare il grafico prima raggruppo per destinazione e poi sommo i vari incassi di ogni gruppo
incasso_destinazioni = dati_agenzia.groupby("Destinazioni")["Incasso"].sum()
plt.bar(destinazioni_possibili, incasso_destinazioni, color = "orange")
plt.title("Incassi per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso ($)")
plt.show()

#faccio il grafico a linee che mostra l'andamento giornaliero degli incassi
incassi_giornalieri = np.random.randint(200, 2000, size = 10)
ore_giorno = [9, 10, 11, 12, 13, 16, 17, 18, 19, 20]
plt.figure(figsize = (8, 5))
plt.plot(ore_giorno, incassi_giornalieri, color = "skyblue")
plt.xlabel("ora (h)")
plt.ylabel("Incassi $")
plt.title("Andamento giornaliero degli incassi")
plt.show()

#faccio il grafico a torta per mostrare la % di vendite per destinazione
vendite_per_destinazione = dati_agenzia["Destinazioni"].value_counts()
plt.figure(figsize = (8,5))
plt.pie(vendite_per_destinazione, explode = None, colors = None, autopct= "%1.1f%%" )
plt.title("Vendite per destinazione (%)")
plt.legend(labels=vendite_per_destinazione.index, title = "Destinazioni", loc = "center left", bbox_to_anchor = (1, 0.5))
plt.show()

#Parte 6: Analisi avanzata
#Creiamo il dizionario che associa la città al continente
categorie_viaggi = {"Roma" : "Europa" ,
                    "Parigi" : "Europa",
                    "Londra": "Europa",
                    "Tokyo" : "Asia",
                    "New York": "America"                
                    }
continenti_disponibili = ["Europa", "Asia", "America"]
#Aggiungiamo una nuova colonna al DataFrame che riporta i dati dell'agenzia che colleghi il continente alla prenotazione
dati_agenzia["Continente"] = dati_agenzia["Destinazioni"].map(categorie_viaggi)
#Calcoliamo l'incasso totale per categoria.
incasso_continenti = dati_agenzia.groupby("Continente")["Incasso"].sum()
durata_media_continenti = dati_agenzia.groupby("Continente")["Durata"].mean()
analisi_prenotazioni = pd.DataFrame ({
    "Incasso per continenti ($)": incasso_continenti,
    "Durata media viaggi (giorni)" : durata_media_continenti
})

print(analisi_prenotazioni)
analisi_prenotazioni.to_csv("prenotazioni_analizzate.csv")

#Parte 7: Estensioni
"""Anche se la consegna chiede i clienti con più prenotazioni, avendo impostato il codice con tutti clienti diversi che hanno
effettuato una prenotazione sola, inserirò i clienti che hanno speso di più"""
#Ordino il DataFrame in modo da avere i clienti che hanno speso di più nelle prime posizioni ci sia chi ha speso di più
dati_agenzia_ordinati = dati_agenzia.sort_values(by = "Incasso", ascending=False)
clienti_migliori = dati_agenzia_ordinati[["Clienti", "Incasso"]].head(5)
print(f"\n========= CLIENTI MIGLIORI ===========\n{clienti_migliori}")







