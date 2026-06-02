#============================ PROGETTO FINALE MODULO 1 ============================
#Analisi di Vendite di una catena di negozi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#=============== PARTE 1: Creazione del DataSet ===============
#creo un data set di vendite utilizzando una lista di dizionari
vendite = [ {"Data": "2023-09-01", "Negozio": "Milano", "Prodotto": "Smartphone", "Quantità": 5, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-01", "Negozio": "Roma", "Prodotto": "Laptop", "Quantità": 2, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-01", "Negozio": "Napoli", "Prodotto": "TV", "Quantità": 3, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-02", "Negozio": "Milano", "Prodotto": "Tablet", "Quantità": 4, "Prezzo_unitario": 399.99},
    {"Data": "2023-09-02", "Negozio": "Roma", "Prodotto": "Smartphone", "Quantità": 6, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-02", "Negozio": "Napoli", "Prodotto": "Laptop", "Quantità": 1, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-03", "Negozio": "Milano", "Prodotto": "TV", "Quantità": 2, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-03", "Negozio": "Roma", "Prodotto": "Tablet", "Quantità": 5, "Prezzo_unitario": 399.99},
    {"Data": "2023-09-03", "Negozio": "Napoli", "Prodotto": "Smartphone", "Quantità": 4, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-04", "Negozio": "Milano", "Prodotto": "Laptop", "Quantità": 3, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-04", "Negozio": "Roma", "Prodotto": "TV", "Quantità": 2, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-04", "Negozio": "Napoli", "Prodotto": "Tablet", "Quantità": 6, "Prezzo_unitario": 399.99},
    {"Data": "2023-09-05", "Negozio": "Milano", "Prodotto": "Smartphone", "Quantità": 7, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-05", "Negozio": "Roma", "Prodotto": "Laptop", "Quantità": 2, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-05", "Negozio": "Napoli", "Prodotto": "TV", "Quantità": 1, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-06", "Negozio": "Milano", "Prodotto": "Cuffie", "Quantità": 8, "Prezzo_unitario": 149.99},
    {"Data": "2023-09-06", "Negozio": "Roma", "Prodotto": "Smartwatch", "Quantità": 4, "Prezzo_unitario": 299.99},
    {"Data": "2023-09-06", "Negozio": "Napoli", "Prodotto": "Cuffie", "Quantità": 5, "Prezzo_unitario": 149.99},
    {"Data": "2023-09-07", "Negozio": "Milano", "Prodotto": "Smartwatch", "Quantità": 3, "Prezzo_unitario": 299.99},
    {"Data": "2023-09-07", "Negozio": "Roma", "Prodotto": "Smartphone", "Quantità": 5, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-07", "Negozio": "Napoli", "Prodotto": "Laptop", "Quantità": 2, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-08", "Negozio": "Milano", "Prodotto": "Tablet", "Quantità": 4, "Prezzo_unitario": 399.99},
    {"Data": "2023-09-08", "Negozio": "Roma", "Prodotto": "Cuffie", "Quantità": 7, "Prezzo_unitario": 149.99},
    {"Data": "2023-09-08", "Negozio": "Napoli", "Prodotto": "Smartwatch", "Quantità": 3, "Prezzo_unitario": 299.99},
    {"Data": "2023-09-09", "Negozio": "Milano", "Prodotto": "TV", "Quantità": 2, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-09", "Negozio": "Roma", "Prodotto": "Tablet", "Quantità": 4, "Prezzo_unitario": 399.99},
    {"Data": "2023-09-09", "Negozio": "Napoli", "Prodotto": "Smartphone", "Quantità": 6, "Prezzo_unitario": 699.99},
    {"Data": "2023-09-10", "Negozio": "Milano", "Prodotto": "Laptop", "Quantità": 1, "Prezzo_unitario": 1199.99},
    {"Data": "2023-09-10", "Negozio": "Roma", "Prodotto": "TV", "Quantità": 3, "Prezzo_unitario": 899.99},
    {"Data": "2023-09-10", "Negozio": "Napoli", "Prodotto": "Cuffie", "Quantità": 9, "Prezzo_unitario": 149.99}]

#creo il DataFrame che verrà utilizzato per stampare il file csv
df = pd.DataFrame(vendite)
#creo il file csv
df.to_csv("Vendite.csv", index = 0)

#=============== PARTE 2: Importo il file csv ===============
dati = pd.read_csv("Vendite.csv")
#Stampo i dati relativi alle prime 5 righe
print(f"Ecco i dati delle prime 5 righe:\n{dati.head(5)}")
print(f"Il numero di righe e colonne è:\n{dati.shape}")
print("Le informazioni riguardo ai dati sono:")
dati.info()

#=============== PARTE 3: Elaborazioni con Pandas ===============
#Aggiungo una colonna Incasso calcolata comequantità * prezzo_unitario
dati["Incasso"] = dati["Quantità"] * dati["Prezzo_unitario"]
print(dati)
#Somma incasso complessivo di tutta la catena
incasso_complessivo = dati["Incasso"].sum()
print(f"L'incasso complessivo della catena è:\n{incasso_complessivo:.2f}€")
#Calcolo l'incasso medio per ogni negozio
incasso_medio_negozi = dati.groupby("Negozio")["Incasso"].mean()
print(f"L'incasso medio per negozio è: {incasso_medio_negozi}€")
#Calcolo i 3 prodotti più venduti
#Raggruppo per prodotto e sommo le quantità
prodotti_venduti = dati.groupby("Prodotto")["Quantità"].sum()
#Oridno i prodotti in modo decrescente in base alle quantità vendute
prodotti_più_venduti = prodotti_venduti.sort_values(ascending=False)
#Stampo i 3 prodotti più venduti
print(f"I prodotto più venduti sono:\n{prodotti_più_venduti.head(3)}")
#Raggruppo i dati per Negozio e Prodotto e calcolo incasso medio
#Raggruppo per negozio
incasso_medio_negozio_prodotto = dati.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print(f"Per ogni negozio, l'incasso medio di ogni prodotto è:\n{incasso_medio_negozio_prodotto}€")

#=============== PARTE 4: Uso di Numpy ===============
#Trasformo le colonne quantità e prezzo unitario del dataframe in un array 2D in numpy 
quantità_prezzo = dati[["Quantità", "Prezzo_unitario"]].to_numpy()
print(quantità_prezzo)
#calcolo l'incasso per ogni riga
incasso_check = quantità_prezzo[:,0]*quantità_prezzo[:,1]
print(incasso_check)
#controllo che l'incasso trovato sia uguale a quello del DataFrame
check = incasso_check == dati["Incasso"]
print(check)

#=============== PARTE 5: Visualizzazioni con Matplotlib ===============
#Creo il grafico a barre che rappresenta l'incasso totale per ogni negozio
#Raggruppo i dati per negozio e sommo gli incassi per ogni gruppo
incasso_totale_negozi = dati.groupby("Negozio")["Incasso"].sum()
plt.figure(figsize=(8,5))
plt.bar(incasso_totale_negozi.index, incasso_totale_negozi.values, color = "skyblue")
plt.title("Incasso totale per ogni negozio")
plt.xlabel("Negozi")
plt.ylabel("Incasso totale")
plt.show()

#Creo il grafico a torta che rappresenta la percentuale di incassi per ciascun prodotto
#Raggruppo i dati per prodotto e calcolo l'incasso totale di ogni prodotto
incasso_totale_prodotti = dati.groupby("Prodotto")["Incasso"].sum()
plt.figure(figsize=(8,5))
plt.pie(incasso_totale_prodotti, autopct= "%1.1f%%")
plt.title("Incasso per prodotto")
plt.legend(labels=incasso_totale_prodotti.index, title = "Prodotti", loc = "center left", bbox_to_anchor = (1, 0.5))
plt.show()

#Creo il grafico a barre che rappresenta l'andamento giornaliero degli incassi totali della catena
#Raggruppo il DataFrame per giorni e sommo l'incasso totale in ogni giorno
incassi_per_giorno = dati.groupby("Data")["Incasso"].sum()
plt.figure(figsize=(8,5))
plt.plot(incassi_per_giorno.index, incassi_per_giorno.values, color = "green")
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Giorno")
plt.ylabel("Incasso totale della catena")
plt.show()

#=============== PARTE 6: Analisi avanzata ===============
#Creo una nuova colonna "Categoria" che raggruppi i prodotti in grandi famiglie
Categoria = {
    "Smartwatch" : "Telefonia",
    "Smartphone" : "Telefonia",
    "Tablet" : "Informatica",
    "Laptop" : "Informatica",
    "TV" : "Intrattenimento",
    "Cuffie" : "Intrattenimento" 
}
dati["Categoria"] = dati["Prodotto"].map(Categoria)
print(dati)
