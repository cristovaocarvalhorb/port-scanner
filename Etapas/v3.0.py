#Recebmento de input do usuário.
#Tratamento de erros com try/except.

import socket
import sys

alvo = input("Digite o endereço (IP ou Domínio) que deseja escanear:")

print("-" * 50)
print(f"GhostProbe escaneando: {alvo}")
print("-" * 50)

try:
    for porta in range(1, 101):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        cliente.settimeout(0.1)

        resultado=cliente.connect_ex((alvo, porta))

        if resultado == 0:
            print(f"Porta {porta} aberta em {alvo}")
        
        cliente.close()

except socket.gaierror:
    print("\nO alvo não pôde ser encontrado. Verifique o endereço digitado.")
    sys.exit()

except KeyboardInterrupt:
    print("\nSaindo do programa...")
    sys.exit()

except socket.error:
    print(f"\nNão foi possível se conectar à {alvo}")
    sys.exit()

print("-" * 50)
print("Escaneamento finalizado.")