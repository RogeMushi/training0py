idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")


        # < - menor que
        # > - maior que
        # <= - menor ou igual
        # >= - maior ou igual a
        # == - igual a
        # != - diferente de


# usuario = input("Informe o usuário do sistema!")
#
# if(usuario == "Flávio"):
#     print("Seja bem-vindo Flávio!")
# elif(usuario == "Douglas"):
#     print("Seja bem-vindo Douglas!")
# elif(usuario == "Nico"):
#     print("Seja bem-vindo Nico")
# else:
#     print("Usuário não identificado!")