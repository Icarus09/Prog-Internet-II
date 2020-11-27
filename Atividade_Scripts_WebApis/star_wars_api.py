import json
import requests


def main():

    print("uma api de Star Wars")
    print("1. people\n2. planets\n3. starships\n")

    while (True):

        response = requests.get("https://swapi.dev/api")
        opcao = int(input("Opção: "))

        if opcao == 1:
            id = input("Digite o id do personagem: ")
            nova_url = response.url +"people/"+ str(id)  
            response = requests.get(nova_url) 
            personagem = json.loads(response.content)
            print("personagem\n")
            print("Personagem: %s" % personagem["name"])
            print("Gereno: %s" % personagem["gender"])


        elif opcao == 2:
            id = input("Digite o id do planeta: ")
            nova_url = response.url +"planets/"+ str(id)
            response = requests.get(nova_url)
            planeta = json.loads(response.content)
            print("Planeta\n")
            print("Nome: %s" % planeta["name"])
            print("Clima: %s" % planeta["climate"])
            print("Populacao: %s" % planeta["population"])

        elif opcao == 3:
            id = input("Digite o id da Nave: ")
            nova_url = response.url + "starships/" + str(id)
            response = requests.get(nova_url) 
            nave = json.loads(response.content)
            print("Nave\n")
            print("Nome: %s" % nave["name"])
            print("Modelo: %s" % nave["model"])
            print("Tamanho: %s" % nave["length"])

        elif opcao == 0:
            break
        else:
            print('Opcao Invalida!')

if __name__ == '__main__':
	main()