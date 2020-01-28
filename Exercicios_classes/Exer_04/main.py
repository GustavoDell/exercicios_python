from Exer_04 import Pessoa

def main():
     nome = input("Digite seu nome: ")
     idade = int(input("Digite sua idade: "))
     peso = float(input("Digite seu peso: "))
     altura = float(input("Digite seu altura: "))
     
     
     continua = True
     
     pessoa = Pessoa(nome, idade, peso, altura) 
     
     while(continua):
        
        print("1.Envelhecer")   
        print("2.Engordar")
        print("3.Emagrecer")
        print("4.Crescer")
        print("5.Sair")
        
        escolha = int(input("Digite uma opção: "))
        
         
        if(escolha == 1):
             pessoa.envelhecer()
             print("{} você envelheceu 1 ano sua idade é de {}".format(pessoa.nome, pessoa.idade))
             if(pessoa.idade < 21):
                 print("Você cresceu 0.5 cm e sua altura é de {}m".format(round(pessoa.altura, 2)))
        elif(escolha == 2):
            pessoa.engordar()
            print("{} você engordou 1 Kg seu peso é de {}Kg".format(pessoa.nome, pessoa.peso))
        elif(escolha == 3):
            pessoa.emagrecer()
            print("{} você emagreceu 1 Kg seu peso é de {}Kg".format(pessoa.nome, pessoa.peso))
        elif(escolha == 4):
            pessoa.crescer()
            print("{} você cresceu 0.5m sua altura é de {}m".format(pessoa.nome, pessoa.altura))
        else:
            continua = False

if __name__ == "__main__":
    main()