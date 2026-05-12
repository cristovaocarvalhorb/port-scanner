# Verificação de uma única porta.
# O método connect_ex() retorna 0 se a porta estiver aberta e um número de erro se estiver fechada.
# O método connect() retorna None se a porta estiver aberta e um erro se estiver fechada.

import socket

alvo = "google.com"
porta = 80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

resultado = cliente.connect((alvo,porta))

if(resultado==None):
    print(f"A porta {porta} está aberta no alvo {alvo}")

else:
    print(f"A porta {porta} está fechada no alvo {alvo}")

cliente.close()