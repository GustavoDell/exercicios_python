class ContaCorrente:
    
    def __init__(self, numero_conta, nome_correntista, saldo = 0):
        self.conta = numero_conta
        self.nome = nome_correntista
        self.saldo = saldo
    
    def alterar_nome(self, nome):
        self.nome = nome

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor