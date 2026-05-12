import socket

alvo = "google.com"

# [CONCEITO] — O 'range(20, 81)' cria uma sequência de 20 até 80.
# No Python, o último número é exclusivo, por isso usamos 81 para chegar até 80.
portas = range(20, 81) 

print(f"Iniciando varredura em: {alvo}")

# [PADRÃO] — O loop 'for' vai pegar uma porta de cada vez da nossa sequência
for porta in portas:
    # [ATENÇÃO] — Criamos um novo socket para CADA porta.
    # Um socket é como um fósforo: você o usa para uma tentativa e depois descarta.
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # [CONCEITO] — Definimos um "Timeout" (tempo de espera).
    # Sem isso, se uma porta não responder, o script pode ficar travado por minutos.
    # Aqui, esperamos apenas 0.5 segundos por porta.
    cliente.settimeout(0.5)

    resultado = cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"Porta {porta} [ABERTA]")
    
    # Fechamos a conexão atual antes de ir para a próxima porta no loop
    cliente.close()

print("Varredura finalizada.")
