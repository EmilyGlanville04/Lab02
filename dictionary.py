class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, parola_aliena, traduzione):
        parola_aliena = parola_aliena.lower()
        traduzione = traduzione.lower()
        if not parola_aliena.isalpha() or not traduzione.isalpha():
            print("Errore: sono ammesse solo lettere a-zA-Z")
            return False
        if parola_aliena not in self.dizionario:
            self.dizionario[parola_aliena] = [traduzione]
        else:
            self.dizionario[parola_aliena].append(traduzione)
        return True

    def translate(self, parola):
        parola = parola.lower()
        return self.dizionario.get(parola, None)

    def translateWordWildCard(self, query):
        query = query.lower()
        risultati_totali = []
        for parola_aliena in self.dizionario.keys():
            if len(parola_aliena) == len(query):
                match = True
                for i in range(len(query)):
                    if query[i] == '?':
                        continue
                    if query[i] != parola_aliena[i]:
                        match = False
                        break
                if match:
                    traduzioni_parola = self.dizionario[parola_aliena]
                    for t in traduzioni_parola:
                        risultati_totali.append(t)
        return risultati_totali if risultati_totali else None


