from tkinter import *  # importa tudo da biblioteca tkinter
from tkinter import ttk  # ttk para trabalhar com temas atualizados

janela = Tk()  # iniciando a janela principal
janela.title("Calculadora")
# janela.geometry("500x500")

mainFrame = ttk.Frame(janela, padding="3 3 12 12")  # criando um WIDGET frame dentro da janela principal
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))  # "centralizando" esse frame em que iremos trabalhar
janela.columnconfigure(0, weight=1)  # TODO: ainda descobrir o sentido desses argumentos
janela.rowconfigure(0, weight=1)

num = StringVar()  # dizendo que NUM é uma variável STRING
num_entrada = ttk.Entry(mainFrame, width=30, justify="right", font="Consolas", textvariable=num)  # widget de entrada, atrelando a variavel NUM que é atualizada constantemente (mérito do tkinter)
num_entrada.grid(row=0, sticky=(W, E, N))  # "centralizando" na janela
# TODO: tabela de botões: os botões da calculadora
sete_botao = ttk.Button(mainFrame, text="7", command="").grid(column=0, row=1)
oito_botao = ttk.Button(mainFrame, text="8", command="").grid(column=1, row=1)
nove_botao = ttk.Button(mainFrame, text="9", command="").grid(column=2, row=1)
clear_botao = ttk.Button(mainFrame, text="C", command="").grid(column=3, row=1)
quatro_botao = ttk.Button(mainFrame, text="4", command="").grid(column=0, row=2)
cinco_botao = ttk.Button(mainFrame, text="5", command="").grid(column=1, row=2)
seis_botao = ttk.Button(mainFrame, text="6", command="").grid(column=2, row=2)
adicao_botao = ttk.Button(mainFrame, text="+", command="").grid(column=3, row=2)
um_botao = ttk.Button(mainFrame, text="1", command="").grid(column=0, row=3)
dois_botao = ttk.Button(mainFrame, text="2", command="").grid(column=1, row=3)
tres_botao = ttk.Button(mainFrame, text="3", command="").grid(column=2, row=3)
subtracao_botao = ttk.Button(mainFrame, text="-", command="").grid(column=3, row=3)
zero_botao = ttk.Button(mainFrame, text="0", command="").grid(column=0, row=4)
multiplicao_botao = ttk.Button(mainFrame, text="*", command="").grid(column=1, row=4)
divisao_botao = ttk.Button(mainFrame, text="/", command="").grid(column=2, row=4)
igual_botao = ttk.Button(mainFrame, text="=", command="").grid(column=3, row=4)




janela.mainloop()  # mantém a janela aberta

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






