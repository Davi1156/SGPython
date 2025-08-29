lista1 = ["quem qanhou a copa de 2014","e quem ganhou a copa de 2018","quem ganhou a copa de 2022"]
lista2 = ["alemanha" ,"franca", "argentina"]

acertos = 0

for numero in range (3):
    print (lista1[numero])
    resposta=input("qual sua resposta?")
    if resposta==lista2[numero]:
        print("voce acertou")
        acertos = acertos + 1
    elif resposta=="":
        print("nao escreveu nada")
    else:
        print("voce errou")


print("voce certou" + str(acertos)) 
