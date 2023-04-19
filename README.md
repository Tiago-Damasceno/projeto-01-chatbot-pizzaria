# CHATBOT PIZZARIA NO PYTHON

* Chatbot feito com Python para realização de acolhida, atendimento e pedido totalmente automatizado.
A ideia original era fazer um bot feito com python para Whatsapp, mas para isso primeiramente fizemos um teste com as duas tecnologias
para ver se era possivel realizar esse tipo de mesclagem, o que chamamos de FASE 1 e FASE 2, caso aprovado a FASE 3 será a fusão dos dois processos para a criação do bot final.

## 📋 Pré-requisitos

* PYTHON 3.11
* TWILIO
* NGROK

## 🔧 Instalação

#### CHATBOT PYTHON (FASE 1):
```
  import (os)
   def (start)
   def (precessar resposta)
```
* Importei o "os" para poder realizar as devidas formatações.
* Defini um start para ele rodar da melhor maneira possivel. 
* Então defini um banco de respostas para cada sabor de pizza pre-pronto. 

###### Exemplo:

_[1] - Calabresa: muçarela, calabresa e cebola. Como não amar?_

#### CHATBOTZAP (FASE 2):
```
  from flask import Flask, request
  from twilio.twiml.messaging_response import MessagingResponse
```
* O Flask é necessario para criar um IP para o programa do Python.
* O twilio é necessario para usar as ferramentas compativeis com a platarforma twilio.

###### Exemplo:

_orignal_msg = request.values.get('body', '')_

## ⚙️ Executando os testes

* Os testes do CHATBOT PYTHON foram realizados no próprio console do VSCode.
* Já os testes CHATBOTZAP foram realizados em um *localhost* implantados pelo FLASK


## 📦 Implantação

Se os testes que faremos forem satisfatorios para nosso cliente, poderemos fazer a implantação de duas maneiras:
* Uma ligação direta com o twilio usando a plataforma ja existente neles.
* Uma construção totalmente em python, mais completa e densa, e o twilio sera usado apenas como *host*.
Será gerada um IP que sera substituido pelo o IP da Twilio. 

## 🛠️ Construído com

* Flask
* twilio
* def
* os

## 📌 Versão

v. 0.1.1.1

## ✒️ Autores

* Criador: Tiago Damasceno

## 📄 Licença

* Licensiado por Tiago Silva Damasceno (devtiago01@gmail.com)

🎁 Gratidão
* Quero agradecer a minha familia que esta me apoiando incondicionalmente no projeto.
* Aos meus colegas de mentoria que sempre me ajudam.
* Aos tutores que são sempre solicitos quando *online*
* Ao Pedro e ao Henrique meus mentores
* A Deus! sem ele nem aqui eu estaria. 
