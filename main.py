# from tkinter import *  # importa tudo da biblioteca tkinter

# lógica básica

while True:  # executa infinitamente
    print("Digite o primeiro número")
    num = float(input())
    print("Digite o operador matemático")
    operacao = input()
    print("Digite outro número")
    num2 = float(input())
    if operacao == "+":
        resultado = num + num2
    elif operacao == "-":
        resultado = num - num2
    elif operacao == "*":
        resultado = num * num2
    elif operacao == "/":
        resultado = num / num2
    print(type(resultado))
    print("Resposta: {:.1f}".format(resultado))



