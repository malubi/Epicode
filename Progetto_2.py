import numpy as np
#PARTE 1 - TIPI DI DATO:
#PAZIENTE 1
nome1 = "Gianni"
cognome1 = "Sperti"
codice_fiscale1 = "GNSPRT123H67U"
età1 = 26
peso1 = 87.4
analisi1 = ["GLICEMIA", "COLESTEROLO LDL","EMOCROMO"]

#PAZIENTE 2
nome2 = "Anna"
cognome2 = "Tatangelo"
codice_fiscale2 = "NNTNGL123H32U"
età2 = 34
peso2 = 67.3
analisi2 = ["GAMMA GT", "COLESTEROLO HDL","CREATININA"]

#PAZIENTE 3
nome3 = "Luca"
cognome3 = "Giurato"
codice_fiscale3 = "LCGRT123H95U"
età3 = 52
peso3 = 78.4
analisi3 = ["COLESTEROLO LDL", "TRANSAMINASI","EMOCROMO"]

#PARTE 2 - CLASSI E OOP
#Definizione di una classe Paziente che contenga i dati del paziente e che ne restituisca una scheda riepilogativa
class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi

    def scheda_personale(self):
        return f"\n---SCHEDA PAZIENTE---\nNome: {self.nome};\nCognome: {self.cognome};\nCodice Fiscale: {self.codice_fiscale};\nEtà: {self.età}\nPeso: {self.peso};\nAnalisi effettuate: {self.analisi_effettuate}"
    
    def statistiche_analisi(self):
        media_risultati = np.mean(self.risultati_analisi)
        minimo_risultati = np.min(self.risultati_analisi)
        massimo_risultati = np.max(self.risultati_analisi)
        dev_risultati = np.std(self.risultati_analisi)
        return F"\nMedia valori: {media_risultati},\nValore massimo: {massimo_risultati},\nValore minimo: {minimo_risultati},\nDeviazione standard risultati: {dev_risultati}"
        
#Definizione di una classe medico che contenga i dati del medico e che stampi una scheda riepilogativa e che indichi il paziente in visita
class Medico:
    def __init__(self, nome_medico, cognome_medico, specializzazione):
        self.nome_medico = nome_medico
        self.cognome_medico = cognome_medico
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"\nMedico di riferimento:\nNome: {self.nome_medico};\nCognome: {self.cognome_medico};\nSpecializzazione: {self.specializzazione}\nPaziente: {paziente.nome}")

#Definizione di una classe analisi che contenga il tipo di analisi svolte e il risultato numerico
class Analisi:
    def __init__(self, analisi_controllate, risultato):
        self.analisi_controllate = analisi_controllate
        self.risultato = risultato

    def valuta(self):

        #creo un dizionario in cui inserire i valori limite di ogni tipologia di analisi
        valori_massimi = {
            "glicemia" : 100,
            "colesterolo ldl" : 200,
            "emocromo" : 300,
            "colesterolo hdl" : 150,
            "transaminasi" : 25,
            "gamma gt" : 76,
            "creatinina" : 204
        }
        #Faccio in modo che le analisi inserite siano sempre in minuscolo
        nome_analisi = self.analisi_controllate.lower()
        
        if nome_analisi in valori_massimi:
            limite = valori_massimi[nome_analisi]

            if self.risultato >= limite:
                print(f"Il valore di {nome_analisi} richiede un approfondimento da parte del suo medico.")
        else:
            print("Analisi non presente")

#PARTE 3 - Uso di NumPy
#creo un array che contenga i risultati della glicemia di 10 pazienti
risultati_glicemia = np.array([98, 47, 105, 99, 65.7, 100, 78.8, 86.5, 96, 114.8])

#Calcolo media, valore massimo, valore minimo e deviazione standard
media_glicemia = np.mean(risultati_glicemia)
massimo_glicemia = np.max(risultati_glicemia)
minimo_glicemia = np.min(risultati_glicemia)
dev_stand_glicemie = np.std(risultati_glicemia)

#BLOCCO PRINCIPALE: MAIN
#Definiamo i 3 medici
medico1 = Medico("Gregory", "House", "Diagnostica")
medico2 = Medico("Lisa", "Cuddy", "Cardiologa")
medico3 = Medico("Eric", "Foreman", "Neurologo")

#Creiamo i 5 pazienti

risultati1 = np.array([110.5, 205.0, 198.2])
paziente1 = Paziente("Gianni","Sperti", "GNSPRT123H67U", 26, 87.4, ["GLICEMIA", "COLESTEROLO HDL", "EMOCROMO"], risultati1)

risultati2 = np.array([90.7, 19.0, 198.2])
paziente2 = Paziente("Anna","Tatangelo", "NNTNGL123H32U", 34, 67.3, ["EMOCROMO", "GLICEMIA", "TRANSAMINASI"], risultati2)

risultati3 = np.array([87.3, 205.0, 198.2])
paziente3 = Paziente("Luca","Giurato", "LCGRT123H95U", 52, 78.4, ["GAMMA GT", "COLESTEROLO HDL","CREATININA"], risultati3)

risultati4 = np.array([170.1, 75.0, 198.2])
paziente4 = Paziente("Hermione","Granger", "HRMNGR123H32U", 14, 47.3, ["GAMMA GT", "COLESTEROLO LDL","EMOCROMO"], risultati4)

risultati5 = np.array([10.2, 205.0, 198.2])
paziente5 = Paziente("Percy","Jackson", "PRSJCKS123H95U", 22, 70.8, ["TRANSAMINASI", "EMOCROMO", "CREATININA"], risultati5)

#Stampiamo le schede paziente
print(paziente1.scheda_personale())
print(paziente1.statistiche_analisi())

print(paziente2.scheda_personale())
print(paziente2.statistiche_analisi())
print(paziente3.scheda_personale())
print(paziente3.statistiche_analisi())
print(paziente4.scheda_personale())
print(paziente4.statistiche_analisi())
print(paziente5.scheda_personale())
print(paziente5.statistiche_analisi())

#Stampiamo le schede medico:
medico1.visita_paziente(paziente3)
medico2.visita_paziente(paziente5)
medico1.visita_paziente(paziente1)
medico3.visita_paziente(paziente4)
medico3.visita_paziente(paziente2)

#Utilizziamo il metodo valuta() nella classe Analisi per capire se le analisi vanno bene

print(f"\nValutazione esame del paziente {paziente1.nome} {paziente1.cognome}")
esame1_paziente1 = Analisi(paziente1.analisi_effettuate[0], paziente1.risultati_analisi[0])
esame1_paziente1.valuta()

esame2_paziente1 = Analisi(paziente1.analisi_effettuate[1], paziente1.risultati_analisi[1])
esame2_paziente1.valuta()

esame3_paziente1 = Analisi(paziente1.analisi_effettuate[2], paziente1.risultati_analisi[2])
esame3_paziente1.valuta()

print(f"\nValutazione esame del paziente {paziente2.nome} {paziente2.cognome}")
esame1_paziente2 = Analisi(paziente2.analisi_effettuate[0], paziente2.risultati_analisi[0])
esame1_paziente2.valuta()

esame2_paziente2 = Analisi(paziente2.analisi_effettuate[1], paziente2.risultati_analisi[1])
esame2_paziente2.valuta()

esame3_paziente2 = Analisi(paziente2.analisi_effettuate[2], paziente2.risultati_analisi[2])
esame3_paziente2.valuta()

print(f"\nValutazione esame del paziente {paziente3.nome} {paziente3.cognome}")
esame1_paziente3 = Analisi(paziente3.analisi_effettuate[0], paziente3.risultati_analisi[0])
esame1_paziente3.valuta()

esame2_paziente3 = Analisi(paziente3.analisi_effettuate[1], paziente3.risultati_analisi[1])
esame2_paziente3.valuta()

esame3_paziente3 = Analisi(paziente3.analisi_effettuate[2], paziente3.risultati_analisi[2])
esame3_paziente3.valuta()

print(f"\nValutazione esame del paziente {paziente4.nome} {paziente4.cognome}")
esame1_paziente4 = Analisi(paziente4.analisi_effettuate[0], paziente4.risultati_analisi[0])
esame1_paziente4.valuta()

esame2_paziente4 = Analisi(paziente4.analisi_effettuate[1], paziente4.risultati_analisi[1])
esame2_paziente4.valuta()

esame3_paziente4 = Analisi(paziente4.analisi_effettuate[2], paziente4.risultati_analisi[2])
esame3_paziente4.valuta()

print(f"\nValutazione esame del paziente {paziente5.nome} {paziente5.cognome}")
esame1_paziente5 = Analisi(paziente5.analisi_effettuate[0], paziente5.risultati_analisi[0])
esame1_paziente5.valuta()

esame2_paziente5 = Analisi(paziente5.analisi_effettuate[1], paziente5.risultati_analisi[1])
esame2_paziente5.valuta()

esame3_paziente5 = Analisi(paziente5.analisi_effettuate[2], paziente5.risultati_analisi[2])
esame3_paziente5.valuta()
