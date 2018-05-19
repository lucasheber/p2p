# coding: utf-8

'''
    O Programa abaixo faz a implementação do cliente P2P.

    O arquivo a ser enviado deve ser colocado na linha 32.
    OBS.: O tipo do arquivo ( extensao ) tem que ser o mesmo que o tipo
          colocado no servidor na linha 48.

    Python: 2.7
    Autor: Lucas Heber
'''

import socket

print "Cliente"

# Coloca o IP do servidor
HOST = '10.0.0.1'

# Porta de conexao com o servidor
PORT = 57000

# Inicia o TCP
s = socket.socket( socket.AF_INET,socket.SOCK_STREAM )

# Realiza a conexao com o servidor
s.connect( (HOST, PORT) )

print "Conexao estabelecida com servidor!"
print "abrindo arquivo..."

# Abre o arquivo que será enviado pro servidor
arquivo = open( 'Projeto Java 16 - Tratamento de Exceções.zip', 'rb' )

print "Realizando a transferencia."

# Le os bytes de cada linha e envia para o servidor
# Poderia pensar que o procedimento abaixo está criando varios pacotes e enviando um por um?
for i in arquivo.readlines():
    # print i
    s.send(i)

print "Arquivo enviado com sucesso!"

# Fecha o arquivo
arquivo.close()

# Fecha a conexao com o servidor
s.close()
