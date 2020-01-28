from Exer_05 import ContaCorrente

def main():

    conta_corrente = ContaCorrente(25, "Gustavo") 

    logado = True 
    while(logado):
        
        print("1.Alterar nome")   
        print("2.Depositar")
        print("3.Sacar")
        print("4.Sair")
        
        escolha = int(input("Digite uma opção: "))
        
         
        if(escolha == 1):
            nome =  input("Digite um nome: ")
            conta_corrente.alterar_nome(nome)
            print("Nome alterado para {}, com sucesso!".format(conta_corrente.nome))
        elif(escolha == 2):
            valor = int(input("Digite o valor do deposito: "))
            conta_corrente.depositar(valor)
            print("Saldo da sua conta é de {}".format(conta_corrente.saldo))
        elif(escolha == 3):
            valor = int(input("Digite o valor do saque: "))
            conta_corrente.sacar(valor)
            print("Saldo da sua conta é de {}".format(conta_corrente.saldo))
        else:
            logado = False

if __name__ == "__main__":
    main()