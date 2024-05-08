class PasswordDB:

    def __init__(self, file_store):
        self.file_store = file_store
        self.passwords = dict()
        self.inizializza_passwords()

    def inizializza_passwords(self):
        file = open(self.file_store)
        for riga in file:
            riga = riga.strip()
            nome_sito, password = riga.split(":")
            self.passwords[nome_sito] = password
        file.close()

    def aggiungi_pasword(self, nome_sito, password):
        if nome_sito in self.passwords:
            print("Il sito è gia nel DB, modifica password.")
            return None
        if ":" in password:
            print("Non puoi usare il carattere ':' nelle tue passord.")
            return None
        if password == (" " * len(password)):
            print("Le password non possono essere bianche.")
            return None

        self.passwords[nome_sito] = password

        file = open(self.file_store, "a")
        file.write("\n")
        file.write(nome_sito)
        file.write(":")
        file.write(password)
        file.close()

    def get_password(self, nome_sito):
        if nome_sito not in self.passwords:
            print(f"Il sito {nome_sito} non è nel DB!")
        else:
            print(f"La password di '{nome_sito}' è '{self.passwords[nome_sito]}'")

    def modifica_password(self, nome_sito, nuova_password):
        if ":" in nuova_password:
            print("Non puoi usare il carattere ':' nelle tue passord.")
            return None
        if nuova_password == (" " * len(nuova_password)):
            print("Le password non possono essere bianche.")
            return None

        self.passwords[nome_sito] = nuova_password
        self.sincronizza_db()

    def sincronizza_db(self):
        file = open(self.file_store, "w")
        for nome_sito, password in self.passwords.items():
            file.write(f"{nome_sito}:{password}\n")
        file.close()

    def elimina_password(self, nome_sito):
        if nome_sito not in self.passwords:
            print("Il sito non è nel DB")
        else:
            del self.passwords[nome_sito]
            self.sincronizza_db()


password_db = PasswordDB(
    "/Users/edoardobarba/misc/fondamenti-di-informatica-2024/lezione-26042024/db_passwords.txt"
)
password_db.get_password("google.com")
password_db.get_password("youtube.com")
password_db.aggiungi_pasword("reddit.com", "ciaociao")
password_db.aggiungi_pasword("flickr.com", "ciaociao")
password_db.modifica_password("flickr.com", "ciaociao2")
password_db.elimina_password("flickr.com")
