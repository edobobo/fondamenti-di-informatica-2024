def check_password_vuota(password):
    return len(password) == 0 or password == (" " * len(password))


class DBPassword:
    """
    Classe che implementa un Database in cui si possono inserire,
    modificare, rimuovere e cercare password per siti web.
    """

    def __init__(self):
        self.store = {}

    def aggiungi_password(self, sito_web, password):
        if check_password_vuota(password):
            print("La password non può essere vuota.")
        elif sito_web in self.store:
            print("Il sito web è già presente!")
        else:
            self.store[sito_web] = password

    def modifica_password(self, sito_web, password):
        if check_password_vuota(password):
            print("La password non può essere vuota.")
        elif sito_web not in self.store:
            print("Il sito web non è nel tuo database.")
        else:
            self.store[sito_web] = password

    def rimuovi_password(self, sito_web):
        if sito_web not in self.store:
            print("Il sito web non è nel tuo database.")
        else:
            del self.store[sito_web]

    def get_password(self, sito_web):
        if sito_web not in self.store:
            print("Il sito web non è nel tuo database.")
        else:
            return self.store[sito_web]

    def stampa_db(self):
        print(self.store)


db = DBPassword()
db.aggiungi_password("facebook", "12345")
db.stampa_db()
db.aggiungi_password("google", "54321")
db.stampa_db()
db.rimuovi_password("facebook")
db.stampa_db()
db.rimuovi_password("facebook")
db.stampa_db()
db.modifica_password("google", "password123")
db.stampa_db()
db.modifica_password("facebook", "213556afddfadfas")
