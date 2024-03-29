# -*- coding: utf-8 -*-
'''
Client python
Este codigo deve ser iniciado para conectar-se ao server ja iniciado
'''

import socket
import select
import sys

# criando um socket para a conexão
# AF_INET : define a familia de IP que sera utilizada (AF_ de Address Family)
# SOCK_STREAM : define o tipo de conexao do socket, sendo este utilizado para TCP e SOCK_DGRAM para uma conexao UDP
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Por favor, digite apos o nome do script o IP e a porta desejada, ambos separados por um espaco.")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

# Conectando-se ao server
conn.connect((IP_address, Port))

'''
Fazendo uso da biblioteca select, monitoramos dois buffers de leitura: 
    stdin: entrada padrão do sistema (teclado)
    conn: socket usado para a conexão com o server
    
Quando um desses buffers fizer alguma leitura será "pego" pelo select, então comparamos
o buffer para verificarmos se é o socket ou a entrada padrão (stdin): 
    -> Se for o socket, então o "if" será verdadeiro, e imprimimos a mensagem recebida na tela do usuário.
    -> Se for a entrada padrão, então "else" será verdadeiro, e enviaremos a mensagem digitada pelo usuário para o server,
    além de imprimi-la na tela também
'''
while True:
    sockets_list = [sys.stdin, conn]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == conn:
            message = socks.recv(2048).decode(encoding='utf_8', errors='strict')
            print(message)
        else:
            message = sys.stdin.readline()
            conn.send(message.encode(encoding='utf_8', errors='strict'))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()