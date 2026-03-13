import dictionary as d

class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()


    def printMenu(self):
        print("--------------------------\n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit")
        print("--------------------------")

    def loadDictionary(self, nomeFile):
        with open(nomeFile, "r", encoding="UTF-8") as file:
            for riga in file:
                riga = riga.strip()
                if " " in riga:
                    parola, significato = riga.split(" ", 1)
                    self.dizionario.addWord(parola,significato)


    def handleAdd(self, entry):
        parti = entry.split()
        if len(parti)<2:
            raise ValueError("Inserimento non valido")
        parola = parti[0]
        traduzioni = parti[1:]
        for traduzione in traduzioni:
            self.dizionario.addWord(parola, traduzione)



    def handleTranslate(self, query):
        query = query.strip().lower()
        traduzioni = self.dizionario.translate(query)
        if traduzioni:
            for t in traduzioni:
                print(t)
        else:
            print("Parola non trovata")


    def handleWildCard(self,query):
        query = query.strip().lower()
        if query.count("?") != 1:
            print("Errore: la ricerca richiede esattamente un punto di domanda (?).")
            return
        risultati = self.dizionario.translateWordWildCard(query)
        if risultati:
            print("Traduzioni trovate:")
            for i in range(len(risultati)):
                if i == len(risultati) - 1:
                    print(risultati[i])
                else:
                    print(risultati[i], end=", ")
        else:
            print("Nessuna parola corrisponde alla ricerca.")


