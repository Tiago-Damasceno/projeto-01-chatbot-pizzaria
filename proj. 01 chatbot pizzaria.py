import os
def processar_resposta(resposta, nome ):
   if resposta == '1':
        print(f'{os.linesep}excelente escolha, {nome}! custa R$40,00{os.linesep}')
   elif resposta == '2':
        print(f'{os.linesep}excelente escolha, {nome}! custa R$40,00{os.linesep}')
   elif resposta == '3':
        print(f'{os.linesep}excelente escolha, {nome}! custa R$40,00{os.linesep}')
   elif resposta == '4':
        print(f'{os.linesep}excelente escolha, {nome}! custa R$40,00{os.linesep}')
   else:
        print('digite apenas 1,2,3 ou 4...')



def start():
    if __name__ == '_main_':
        start()

#criando um chatbot para uma pizzaria
#apresentar a empresa
print('bemvindo ao Sabor de Italia!')
#perguntar o nome da pessoa
nome = input('qual seu nome? ')
#encontrar fonte de perguntas
while True:
    resposta = input(f'posso anotar o seu pedido?{os.linesep}[1] - Calabresa: muçarela, calabresa e cebola. Como não amar? {os.linesep}[2] - Portuguesa: ela é feita com presunto, ovos, muçarela e ervilha. Por que não dar uma chance então?'
      f'{os.linesep}[3] - Baiana: Ela é feita com calabresa moída, ovos, pimenta, cebola e um toque de parmesão.uma das mais pedidas por aqui.'
      f'{os.linesep}[4] - Frango Catupiry:Desconfie de pessoas que não gostam de pizza de frango com catupiry.{os.linesep}')
#ter uma fonte de respostas
    processar_resposta(resposta,nome)

#respostas estão no cardápio da pizzaria

#definir um proprosito
#responder aos clientes de forma mais rapida e acertiva na hora de fazer o pedido (talvez fechar um pedido)