# -*- coding: utf-8 -*-
# [Minha primeira calculadora em Python]
# [Ela não possui interface gráfica pois quando]
# [Comecei a estudar eu não sabia dominar isso.]

quit = False
while quit == False:
# Inicialização
    print("(-----------------------------------------------------)")
    print("[-- Calculadora --]")
    print("                         ")
    print("{ Sobre a calculadora: }")
    print("> Essa é a minha primeira calculadora em Python <")
    print("                         ")
    print("{ Data de criação da calculadora: }")
    print(" > 8 de janeiro de 2021 >")
    print("                         ")
    print("{ Sobre meus estudos: }")
    print("> Eu comecei a estudar Python em 2 de janeiro de 2021 <")
    print("> Antes disso já sabia o básico de C# e Javascript <")
    print("                         ")
    print("{ Criador da calculadora: }")
    print(" > João Vitor Silva >")
    print("(-----------------------------------------------------)")
# Variáveis
    primeiro_num = int(input("[ Coloque o primeiro número: "))
    segundo_num = int(input("[ Coloque o segundo número: "))
    operador = input("[ Coloque o operador do cálculo (* / - +): ")
    # + Soma , - Subtração, / Divisão, * Multiplicação
# Operações
    # Primeiro número + Segundo número
    if operador == "+":
        resultado = primeiro_num + segundo_num
    # Primeiro número - Segundo número
    if operador == "-":
        resultado = primeiro_num - segundo_num
    # Primeiro número * Segundo número
    if operador == "*":
        resultado = primeiro_num * segundo_num
    # Primeiro número / Segundo número
    if operador == "/":
        resultado = primeiro_num / segundo_num
    
    # Resultado do cálculo
    print("[ O resultado do cálculo é: ",primeiro_num,operador,segundo_num,"=",resultado,"]")
    
# Se o usuário quer continuar na calculadora
    na_calculadora = input("Você quer continuar na calculadora? (Sim/Nao): ")
    if na_calculadora == "Sim" or na_calculadora == "sim" or na_calculadora == "s":
        quit = False
        # Mensagem de continuação
        print("Olha! Obrigado por continuar na minha calculadora! :)")
        print("                         ")
    else: 
        quit = True
        # Mensagem de saída
        print("Me perdoe se eu te decepcionei :( Prometo melhorar!")
        print("                         ")