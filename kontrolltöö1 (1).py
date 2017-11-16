#1
arv1 = int(input("Sisesta 1. arv: "))
arv2 = int(input("Sisestage 2. arv: "))
arv_list = list(range(arv1,arv2))
for arv in arv_list:
        if arv % 2 ==0:
            print(arv)
    
#2
tekst = []


loe = open("kttekst.txt", "r")
tekst = loe.read().split()
amount = 0

SõnadeArv = len(tekst)
print("Sõnu on tekstis: ", SõnadeArv)

for sõna in tekst:
    if len(sõna) < 5:
        amount += 1
print("Sõnad mis on lühemad kui 5 tähte:")
print(amount)


