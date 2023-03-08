
import time
from colorama import Fore
import pyrogram
import json
from pyrogram import filters
import urllib3
from urllib3 import request
from pyrogram.errors import BadRequest

app = pyrogram.Client("my_account")
  


@app.on_message(filters.poll)
async def pegarpoll(client, message):
 try:
   start = time.time()
  #----ID DO BOT GROUP HELP----#
  # if "162726413" in str(message.from_user.id):
   if 1==1:
#----INICIA TIMER, E FILTRA PELO PAIS DA PERGUNTA----#
    a0 = str(message.poll.question)
    a1 = a0.replace('🌆 Qual é o país em que fica "', '', 1)
    a2 = a1.replace('"?', '', 1)
    str(a2)

#----FAZER A REQUEST PARA API DE CIDADE PARA PAÍS----#

    manager = urllib3.PoolManager(num_pools=50)
    cidade2 =f'https://positionstack.com/geo_api.php?query={a2}'
    r = manager.request(url=cidade2, method='GET')
   #----FILTRAR PELO PAÍS DA CIDADE----#
    b3 = json.loads(r.data)['data'][0]['country']
   
    
  #---- ..FILTRO PARA COLETAR O NÚMERO CORRETO PARA A ESPECÍFICA CIDADE..  ----# 
    g0 = list(message.poll.options)[0].text
    g1 = list(message.poll.options)[1].text
    g2 = list(message.poll.options)[2].text
    g3 = list(message.poll.options)[3].text
    
    r1 = f'{Fore.GREEN} Achei na Opção 0 {g0}'
    if g1 in b3: # cadeia de comparação
      await app.vote_poll(chat_id=message.chat.id,message_id=message.id, options=1)
      r1 = f'{Fore.GREEN} Achei na Opção 1 {g1}'
    elif g2 in b3:
      await app.vote_poll(chat_id=message.chat.id,message_id=message.id, options=2)
      r1 = f'{Fore.GREEN} Achei na Opção 2 {g2}'
    elif g3 in b3:
      await app.vote_poll(chat_id=message.chat.id,message_id=message.id, options=3)
      r1 = f'{Fore.GREEN} Achei na Opção 3 {g3}'
    elif g0 in b3 :
      await app.vote_poll(chat_id=message.chat.id,message_id=message.id, options=0)
      r1 =f'{Fore.GREEN} Achei na Opção 0 {g0}'
    else:
      await app.vote_poll(chat_id=message.chat.id,message_id=message.id, options=0)
      r1 =f'{Fore.RED} Nenhuma das opções eram a que eu queria : {b3}, Portanto votei na opção "0"'
    end = time.time()
    ctg = end - start
    print(f'{r1},{Fore.BLUE} e respondi em : {str(round(ctg, 2))} segundos.')
    
 except BadRequest as e:
    u='c'
    
#---- RODA O BOTECO ----#
app.run()