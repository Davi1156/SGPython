idade = float(input("diga sua idade"))
vip = input("tem vip?") 
autorizacao = input("tem autorizacao?")
ingresso = input("tem ingresso?")

if idade >= 18 and ingresso == "True" or vip == "True":
    print ("entrar")
elif  idade < 18  and autorizacao == "True" and ingresso == "True" or vip == "True":
    print ("entrar")
elif idade < 12:
    print ("nao entrar")
else:
    print ("nao pode entrar")
