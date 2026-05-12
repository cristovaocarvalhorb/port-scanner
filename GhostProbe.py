import socket
import sys # [CONCEITO] — Biblioteca para interagir com o sistema (ex: fechar o programa)

# [PADRÃO] — Permitimos que o usuário digite o alvo em tempo real
alvo = input("Digite o endereço (IP ou Domínio) para escanear: ")

print("-" * 50)
print(f"GhostProbe escaneando: {alvo}")
print("-" * 50)

try:
    # [CONCEITO] — Vamos escanear as primeiras 100 portas (o intervalo comum)
    for porta in range(1, 101): 
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # [ATENÇÃO] — Diminuímos o timeout para 0.1s para o scanner ser mais ágil
        cliente.settimeout(0.1)
        
        resultado = cliente.connect_ex((alvo, porta))
        
        if resultado == 0:
            print(f"Porta {porta}: ABERTA")
        
        cliente.close()

# [PADRÃO] — Capturamos erros específicos para dar uma resposta amigável
except socket.gaierror:
    # [CONCEITO] — gaierror acontece quando o DNS não encontra o endereço (ex: erro de digitação)
    print("\n[ERRO] O endereço não pôde ser resolvido. Verifique o alvo.")
    sys.exit()

except KeyboardInterrupt:
    # [REPLICAR] — Captura o CTRL+C do usuário para sair sem erro
    print("\n[!] Saindo do programa...")
    sys.exit()

except socket.error:
    print("\n[ERRO] Não foi possível conectar ao servidor.")
    sys.exit()

print("-" * 50)
print("Escaneamento finalizado.")
