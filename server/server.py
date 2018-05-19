# coding: utf-8

'''
    O Programa abaixo faz a implementação do servidor P2P.

    Por enquanto o nome do arquivo está sendo enviado pelo cliente é um nome que escolhi.
    O ideal é que o primeiro envio do cliente seja o nome do arquivo.

    Python: 2.7
    Autor: Lucas Heber
'''

import socket

print "Server"

# IP do servidor
# O IP deve ser o IP real da máquina, ou seja, não pode ser o loopback (127.0.0.1)
# nem o nome da máquina (localhost)

HOST = "10.0.0.1"

# Define a porta de transferencia.
# Deve ser a mesma porta que o cliente define.
PORT = 57000

# Inicia o TPC
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# Liga a conexao TCP
s.bind( (HOST, PORT) )

print "Escutando a porta..."

# Escutando
s.listen(1)

print "Esperando o envio do arquivo..."

# Esperando o cliente fazer o primeiro envio para aceitação
conn, addr = s.accept()

print "Fazendo a transferencia."

# Cria um nome do arquivo
# OBS.: O tipo do arquivo deve ser o mesmo que o cliente está enviando. Sendo assim se
# se ele enviar um arquivo .txt, deverá alterar o nome abaixo para o mesmo tipo.
arquivo = open('projeto2.zip','wb')

# Le os dados
while True:

    # Recebe os dados do arquivo
    dados = conn.recv(4096)

    # Verifica se acabou a transferencia
    if not dados:
        break

    # Escreve os dados do arquivo
    arquivo.write(dados)

print "Transferencia concluida!"

# Fecha o arquivo
arquivo.close()

# Finaliza a conexao
conn.close()
