# Verificação de múltiplas portas.
# Utilização de loop.
# O método settimeout() define um tempo limite para a conexão, caso não haja resposta o script passa para a próxima porta.

import socket

alvo = "google.com"

portas = range(20, 81)

print(f"Iniciando varredura em: {alvo}")

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.settimeout(0.5)

    resultado=cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"Porta {porta} aberta")
    
    cliente.close()

print("Varredura Finalizada!")
    