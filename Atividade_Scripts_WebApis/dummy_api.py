import json
import requests

def main():
  
  headers = {
    'Accept': '*/*',
    'User-Agent':'request',
  }

  print("1 - Para criar um empregado \n 2 - Para listar empregados \n")

  while(True):
    
    opcao = int(input("Opção: "))

    if opcao == 1:
      nome = str(input("Opção: Digite um nome"))
      salario = int(input("Digite um nome um salario"))
      idade = str(input("Digite um nome uma idade"))

      url = 'http://dummy.restapiexample.com/api/v1/create'

      new_employee = {'name': nome, 'salary': salario, 'age': idade}
      resposta = requests.post(url, headers = headers, data = new_employee)
      print(resposta.status_code)
      resposta_dict = resposta.json()
      print(resposta_dict)

    elif opcao == 2:
      url = 'http://dummy.restapiexample.com/api/v1/employees'
      resposta = requests.get(url, headers = headers)
      resposta_dict = resposta.json()
      print(resposta_dict)

    elif opcao == 0:
        break
    else:
        print('Opcao Invalida!')

if __name__ == '__main__':
	main()