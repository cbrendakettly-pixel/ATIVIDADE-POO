class Conta_bancaria: 
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial  # Saldo inicia com o valor passado
    
    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo}")

# Usuário
conta1 = Conta_bancaria("Pedro Lima", 17000)
conta2 = Conta_bancaria("Ana Lima", 25000)

# Exibir saldo e usuário
conta1.exibir_saldo()
conta2.exibir_saldo()
