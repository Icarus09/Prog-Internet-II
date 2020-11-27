import json
import requests


def main():

  print("api de Pokemon")

  print("1. pokemon\n2. Especies de Pokemon\n3. Items\n")

  while (True):

    response = requests.get("https://pokeapi.co/api/v2/")
    opcao = int(input("Opção: "))

    if opcao == 1:
      id = input("Digite o id do pokemon: ")
      nova_url = response.url +"pokemon/"+ str(id) 
      response = requests.get(nova_url) 
      pokemon = json.loads(response.content) 
      print("Pokemon\n")
      print("Nome: %s" % pokemon["name"])
      print("Experiencia: %s" % pokemon["base_experience"])
      print("Altura: %s" % pokemon["height"])
      print("Abilidades: %s" % pokemon["abilities"][0])
      
    elif opcao == 2:
      id = input("Digite o id do da espécie do pokemon: ")
      nova_url = response.url +"pokemon-species/"+ str(id)  
      response = requests.get(nova_url) 
      especie = json.loads(response.content) 
      print("Especies de Pokemon\n")
      print("Nome: %s" % especie["name"])
      print("Ordem: %s" % especie["order"])
      print("Bebe: %s" % especie["is_baby"])
      print("Lendário: %s" % especie["is_legendary"])


    elif opcao == 3:
        id = input("Digite o id do Item: ")
        nova_url = response.url + "item/" + str(id)  
        response = requests.get(nova_url)  
        item = json.loads(response.content) 
        print("Nave\n")
        print("Nome: %s" % item["name"])
        print("Custo: %s" % item["cost"])
        print("Poder de arremesso: %s" % item["fling_power"][0])
        print("Efeito de arremesso: %s" % item["fling_effect"])


    elif opcao == 0:
        break
    else:
        print('Opcao Invalida!')

if __name__ == '__main__':
	main()