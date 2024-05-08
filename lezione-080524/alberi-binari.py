class AlberoBinario:

    def __init__(self, chiave):
        self.chiave = chiave
        self.figlio_destro = None
        self.figlio_sinistro = None

    def inserisci_figlio_sinistro(self, chiave):
        if self.figlio_sinistro is None:
            self.figlio_sinistro = AlberoBinario(chiave)
        else:
            t = AlberoBinario(chiave)
            t.figlio_sinistro = self.figlio_sinistro
            self.figlio_sinistro = t

    def inserisci_figlio_destro(self, chiave):
        if self.figlio_destro is None:
            self.figlio_destro = AlberoBinario(chiave)
        else:
            t = AlberoBinario(chiave)
            t.figlio_destro = self.figlio_destro
            self.figlio_destro = t

    def stampa_preordine(self, livello):
        print(livello, self.chiave)
        if self.figlio_sinistro is not None:
            self.figlio_sinistro.stampa_preordine(livello + 1)
        if self.figlio_destro is not None:
            self.figlio_destro.stampa_preordine(livello + 1)

    def stampa_postordine(self, livello):
        if self.figlio_sinistro is not None:
            self.figlio_sinistro.stampa_postordine(livello + 1)
        if self.figlio_destro is not None:
            self.figlio_destro.stampa_postordine(livello + 1)
        print(livello, self.chiave)

    def stampa_simmetrica(self, livello):
        if self.figlio_sinistro is not None:
            self.figlio_sinistro.stampa_simmetrica(livello + 1)
        print(livello, self.chiave)
        if self.figlio_destro is not None:
            self.figlio_destro.stampa_simmetrica(livello + 1)


if __name__ == "__main__":
    gerarchia_nlp = AlberoBinario("Navigli")
    gerarchia_nlp.inserisci_figlio_sinistro("Edoardo")
    gerarchia_nlp.inserisci_figlio_sinistro("Simone")
    gerarchia_nlp.inserisci_figlio_destro("Marrella")

    gerarchia_nlp.figlio_sinistro.inserisci_figlio_destro("Martinelli")

    print("Stampa postordine")
    gerarchia_nlp.stampa_postordine(0)
    print()

    print("Stampa preordine")
    gerarchia_nlp.stampa_preordine(0)
    print()

    print("Stampa simmetrica")
    gerarchia_nlp.stampa_simmetrica(0)
    print()
