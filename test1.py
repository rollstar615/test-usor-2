def read_list():
    lista = []
    nr = int(input("Cate numere doriti: "))
    for i in range(nr):
        lista.append(int(input("dati al {}-lea numar: ".format(i + 1))))
    return lista

def palindrom(nr):
    n=nr
    invers=0
    while n>0:
        invers=invers*10+n%10
        n=n//10
    if nr==invers:
        return True

def afisare_ultim_palindrom(lista):
    rezultat=0
    for i in range(len(lista)):
        if palindrom(lista[i])==True:
            rezultat=lista[i]
    return rezultat

def verif_rez():
    assert afisare_ultim_palindrom([22,212,34,56,76,23,33,444,434])==434
    assert afisare_ultim_palindrom([2,3,5,6,33,101,200,303])==303
verif_rez()

def numar_semiprim(nr):
    k=0
    for i in range(1, nr+1):
        if nr%i==0:
            k=k+1
    if k==3:
        return True

def lista_semiprim(lista):
    rezultat=0
    temp=0
    for i in range(len(lista)):
        if numar_semiprim(lista[i])==True:
            temp=lista[i]
    for i in range(len(lista)):
        if numar_semiprim(lista[i])==True:
            rezultat=lista[i]
        if rezultat<temp:
            temp=lista[i]
    return temp

def verificare_semiprim():
    assert lista_semiprim([22,33,4,9,25])==4
    assert lista_semiprim([9,6,5,7,32,4,49])==4
verificare_semiprim()

def cifre_impare(nr):
    k=0
    x=0
    w=0
    while nr>0:
        x=nr%10
        if x%2==1:
            k=k+1
        w=w+1
        nr=nr//10
    if k==w:
        return True

def lista_cifre_impare(lista):
    rezultat=[]
    for i in range(len(lista)):
        if cifre_impare(lista[i])==True:
            rezultat.append(lista[i])
    return rezultat

def verificare_impar():
   assert lista_cifre_impare([33,55,11,22,32,45,34,23])==[33,55,11]
   assert lista_cifre_impare([35,77,99,121,131,3579])==[35,77,99,131,3579]
verificare_impar()

import math

def patrat(nr):
   x=math.sqrt(nr)
   x=x//1
   return x

def radical(nr):
    x=nr*nr
    return x

def functie(lista):
    rezultat=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            rezultat.append(lista[i])
        else:
            rezultat.append([radical(lista[i]),patrat(lista[i])])
    return rezultat

def show_menu():
    print("1.Citire lista")
    print("2.Ceva")
    print("3.Altceva")
    print("4.rasaltceva")
    print("5.cevaceva")
    print ("x.Iesire")

def interface():
    lista=[]
    while True:
        show_menu()
        op=input("optiune:")
        if op=="1":
            lista=read_list()
        elif op=="2":
            print(afisare_ultim_palindrom(lista))
        elif op=="3":
            print(lista_semiprim(lista))
        elif op=="4":
            print(lista_cifre_impare(lista))
        elif op=="5":
            print(functie(lista))
        elif op=="x":
            break
        else:
            print("invalid")
interface()









