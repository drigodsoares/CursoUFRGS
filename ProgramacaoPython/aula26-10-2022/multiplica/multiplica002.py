"""
Programa Soma
Requisito: Este programa pega dois números digitados pelo
usuário e calcula o produto e coloca na tela o resultado obtido,
com uma frase que explique o que é resultado obtido.
Autor: Rodrigo Damasceno Soares
Data: 26/10/2022
Versão 0.1.2
Correção do bug: chamar de parcela o que é, na verdade, fator.
Inclusão de funcionalidade: informarr o usuário para que serve
o programa
"""

# Entrada
print (f"Este programa calcula o produto de dois números dados pelo usuário")
numero1 = float (input("\nDigite o primeiro fator: "))
numero2 = float (input("\nDigite o segundo fator: "))

# Processamento

produto = numero1*numero2

# Saída

print (f"O primeiro número digitado foi {numero1} e o segundo número foi {numero2}. O produto deles é: {produto}")
