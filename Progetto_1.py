#--------------------------PROGETTO1: GESTIONE BIBLIOTECA DIGITALE--------------------------

#Parte1: variabili
#1
titolo = "Il barone rampante"
#2
copie_disp = 3
#3
prezzo_medio = 12.50
#4
stato = copie_disp > 0

print("PARTE1:")
print(f"Titolo: {titolo}\nCopie disponibili: {copie_disp}\nPrezzo: {prezzo_medio}€\nDisponibilità: {stato}\n\n")


#Parte2: Strutture dati
#1
libri = ["Amore e pregiudizio", "Tutta la vita che resta", "Molto forte, incredibilmente vicino", "Una vita come tante", "L'uomo dei cerchi azzurri"]
#2
copie = {libri[0]: 3, libri[1]: 4, libri[2]: 1, libri[3]: 0, libri[4]: 9}
#3
utenti = {"Giorgia Meloni", "Eleazaro Rossi", "Chuck Norris", "Fabrizio Corona", "Vanna Marchi", "Mara Maionchi", "Ambra Angiolini"}

#Parte3: Classi e OOP
#Definisco la classe libro:
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
    
    def info(self):
        print(f"{self.titolo} è stato scritto da {self.autore} nel {self.anno}.\nCopie disponibili: {self.copie_disponibili}")

#Definisco la classe utente con metodo scheda:
class Utente:
    def __init__(self, nome, età, id_utente):
        self.nome = nome
        self.età = età
        self.id_utente = id_utente
    
    def scheda(self):
        return f"Nome utente: {self.nome}\nEtà: {self.età}\nID: {self.id_utente}"
    
#Definisco la classe prestito
class Prestito:
    def __init__ (self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
    def dettagli(self):
        print("DETTAGLI PRESTITO:")
        print(f"Libro: {self.libro.titolo}")
        print(self.utente.scheda())
        print(f"Giorni di prestito: {self.giorni}")

#Definisco la classe presta_libro attraverso la quale diminuisco le copie dei libri prestati:    
def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1
        prestito = Prestito(utente, libro, giorni)
        prestito.dettagli()
        return prestito
    else:
        print()
        print(f"DETTAGLI PRESTITO: ")
        print(utente.scheda())
        print(f"Il libro '{libro.titolo}' non è disponibile\n")

#Definisco utenti e libri diversi:    
utente1 = Utente("Giorgia Meloni", 50, "AB666")
utente2 = Utente("Vanna Marchi", 80, "CX098")
utente3 = Utente("Fabrizio Corona", 55, "AM000")

libro1 = Libro("Amore e pregiudizio", "Jane Austin", 1813, 5)
libro2 = Libro("Molto forte, incredibilmente vicino", "Jonathan Safran Foer", 2005, 0)
libro3 = Libro("Tutta la vita che resta", "Roberta Recchia", 2024, 3)

#Utilizzo il programma di prestito della biblioteca:
print("-----PARTE 3 ---- ")
p1 = presta_libro(utente1, libro1, 12)
p2 = presta_libro(utente2, libro2, 4)
p3 = presta_libro(utente3, libro3, 9)

print()
print("LISTA AGGIORNATA DELLE COPIE DISPONIBILI:")
print(f"{libro1.titolo}: {libro1.copie_disponibili}")
print(f"{libro2.titolo}: {libro2.copie_disponibili}")
print(f"{libro3.titolo}: {libro3.copie_disponibili}")