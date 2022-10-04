# This is an example for the conditional structures
# This programs calculates the The Body Mass Index (BMI) in Metric Units
# it also uses the instruction os.system("cls" if os.name=="nt" else "clear") to clear the console
# You can read data form the user using input

import os

os.system("cls" if os.name=="nt" else "clear")

print("Calculadora de Indice de masa Corporal\n")
weight=float(input("por favopr introduzca su peso en Kg: "))
height=float(input("por favor introduzca su estatura en metros: "))
bmi=float(weight/(height**2))
if bmi<18.5 :
    print (f"Su indice de masa corporal es: {round(bmi,1)}, lo que indica que su peso es bajo")
elif bmi<25 :
    print (f"Su indice de masa corporal es: {round(bmi,1)}, lo que indica que su peso es normal")
elif bmi<30 :
    print (f"Su indice de masa corporal es: {round(bmi,1)}, lo que indica que tiene sobrepeso")
else:
    print (f"Su indice de masa corporal es: {round(bmi,1)}, lo que indica que tiene obesidad")