import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    if txtIn.isdigit() and int(txtIn)<6:
        if int(txtIn) == 1:
            print("Quale parola devo aggiungere?")
            txtIn = input()
        if int(txtIn) == 2:
            print("Quale parola devo cercare?")
            txtIn2= input()
            t.handleTranslate(txtIn2)
        if int(txtIn) == 3:
            print("Quale parola devo cercare?")
            txtIn = input()
        if int(txtIn) == 4:
            pass
        if int(txtIn) == 5:
            break
    else:
        raise ValueError("Valore non valido")
