print("Programa para calcular IMC")

print("Por favor inorme seu peso ==>")
peso = float(input())

print("Por favor informe sua altura em *CM* animal! ==>")
altura = float (input())

imc = peso / ((altura / 100 )**2)
print("Seu IMC é: ", imc)
if imc >= 25:
    print("Você precisa emagrecer.")
else:
    print("Você não precisa emagrecer.")
print("Fim do programa.")