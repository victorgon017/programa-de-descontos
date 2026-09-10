#Programa de cálculo de descontos
#Autor: Victor Gonçalves
#Entrada
Valor = float(input("Insira o valor total da compra: "))
#Processamento
if Valor < 200:
    desconto = Valor * 0.05
elif 200 <= Valor < 300:
    desconto = Valor * 0.10
else: 
    desconto = Valor * 0.15

total_a_pagar = Valor - desconto

#Saída
print(f"Valor do desconto: R${desconto:.2f} ")
print(f"Valor total a pagar: R$ {total_a_pagar:.2f}")