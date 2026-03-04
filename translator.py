import dictionary as d

class Translator:

    def __init__(self):
        self.dict = d.Dictionary()


    def printMenu(self):
        print("--------------------------\n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit")
        print("--------------------------")

    def loadDictionary(self, dict):
        with open(dict, "r", encoding="UTF8") as file:
            for riga in file:
                riga = riga.strip()
                if " " in riga:
                    parola, significato = riga.split(" ", 1)
                    self.dict.addWord(parola,significato)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        query = query.strip().lower()
        if query in self.dict.dizionario:
            print("Traduzione:", self.dict.dizionario[query])
        else:
            print("Parola non trovata")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass