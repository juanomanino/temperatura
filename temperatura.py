"""Programa No. 3
Programa para calcular grados Kelvin y Celsius"""

print("----------------------")
print("---Grados Celsius a Fahrenheit y Kelvin-----")
print("----------------------")

#input
c=int(input("Digite los grados Celsius: "))

#processing
k=c+273.15
f=1.8*c+32

#output
print(str(c)+" grados Celsius son "+str(k)+" grados kelvin y "+str(f)+" grados fahrenheit")

