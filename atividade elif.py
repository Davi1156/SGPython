nota1 = int(input("nota 1 "))
nota2 = int(input("nota 2 "))
nota3 = int(input("nota 3 "))

media = nota1 + nota2 + nota3 
media = media/ 3 

if  media < 5:
    print ("ficou abaixo da media")
elif media == 10: 
    print ("tirou 10 nas 3 notas")
else :
    print ("ficou acima da media")
