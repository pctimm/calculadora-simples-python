from tkinter import *  # importa tudo da biblioteca tkinter

janela = Tk()
janela.title("Calculadora")
janela.geometry("500x450")
text = Text(janela, width=1, height=1)
text.pack()
janela.mainloop()

#while True:  # executa infinitamente
#    num = float(input("Digite o primeiro número"))
#    # debug print(type(num))
#    operacao = input("Digite o operador matemático")
#    # debug print(type(operacao))
#    num2 = float(input("Digite outro número"))
#    # debug print(type(num2))
#    if operacao == "+":
#        resultado = num + num2
#    elif operacao == "-":
#        resultado = num - num2
#    elif operacao == "*":
#        resultado = num * num2
#    elif operacao == "/":
#        resultado = num / num2

    # debug print(type(resultado))
#    print("Resposta: {:.1f}".format(resultado))




