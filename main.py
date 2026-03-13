import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")


while(True):

    t.printMenu()



    txtIn = input()

    # Add input control here!
    if txtIn.isdigit() and int(txtIn)<6:
        if int(txtIn) == 1:
            print("Quale parola devo aggiungere?")
            entry = input().strip()
            if entry:
                t.handleAdd(entry)
            else:
                print("Errore: input vuoto.")
        if int(txtIn) == 2:
            print("Quale parola devo cercare?")
            parola = input().strip()
            if parola:
                t.handleTranslate(parola)
            else:
                print("Errore: inserire una parola.")
        if int(txtIn) == 3:
            print("Quale parola devo cercare?")
            query = input().strip()
            if query:
                t.handleWildCard(query)
            else:
                print("Errore: inserire una parola con '?'.")
        if int(txtIn) == 4:
            diz = t.dizionario.dizionario
            if not diz:
                print("Il dizionario è vuoto.")
            else:
                print("\n--- CONTENUTO DIZIONARIO ---")
                for aliena, traduzioni in diz.items():
                    print(f"Parola aliena: {aliena}")
                    print("Traduzioni:")
                    for trad in traduzioni:
                        print("-", trad)
        if int(txtIn) == 5:
            break
    else:
        raise ValueError("Valore non valido")
