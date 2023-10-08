n=int(input("Donner un nombre : "))
s=0
while n<0 :
    n=int(input("Donner un nombre positif ou null: "))
for i in range(0,n+1):
    s=s+(10**i)
print("la somme est ",s)