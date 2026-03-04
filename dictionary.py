class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, parola_aliena, traduzione):
        parola_aliena = parola_aliena.lower()
        traduzione = traduzione.lower()
        if not parola_aliena.isalpha() or not traduzione.isalpha():
            print("Errore: sono ammesse solo lettere a-zA-Z")
            return False
        self.dizionario[parola_aliena] = traduzione
        return True

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass