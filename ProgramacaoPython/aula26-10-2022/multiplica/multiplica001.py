"""
Programa Soma
Requisito: Este programa pega dois números digitados pelo
usuário e calcula a sua multiplicacao e coloca na tela o resultado obtido,
com uma frase que explique o que é resultado obtido.
Autor: Rodrigo Damasceno Soares
Data: 26/10/2022
Versão 0.0.1
"""

# Entrada

numero1 = float (input("Digite um número: "))
numero2 = float (input("Digite outro número para ser somado ao primeiro "))

# Processamento

soma = numero1*numero2

# Saída

print (f"O primeiro número digitado foi {numero1} e o segundo número foi {numero2}. A multiplicacao deles é: {soma}")
