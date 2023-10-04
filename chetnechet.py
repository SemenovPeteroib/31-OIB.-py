slovo = input('Введите слово с гласными буквами: ')
11
eg=slovo.count('e') # считает количество гласных e

ag=slovo.count('a') # считает количество гласных a

ig=slovo.count('i') # считает количество гласных i

ug=slovo.count('u') # считает количество гласных u

og=slovo.count('o') # считает количество гласных o

schetglas=eg+ag+ig+ug+og # суммирует гласные

print("всего гласных",schetglas) #выводит количество гласных

print("всего согласных",len(slovo)-schetglas)  # считает сколько букв в слове и минусует от общего количества букв гласные, выводит количество согласных

if (eg==0):

    print ("гласной e в слове Нет!")

else:

    print("e=",eg)

if (ug==0):

    print ("гласной u в слове Нет!")

else:

    print("u=",ug)

if (og==0):

    print ("гласной o в слове Нет!")

else:

    print("o=",og)

if (ag==0):

    print ("гласной a в слове Нет!")

else:

    print("a=",ag)

if (ig==0):

    print ("гласной i в слове Нет!")

else:

    print("i=",ig)