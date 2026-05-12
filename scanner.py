import socket # [CONCEITO] — Biblioteca padrão para comunicações de rede (sockets)

# [PADRÃO] — Definimos o alvo (quem vamos testar) e a porta (qual ramal)
# A porta 80 é o padrão para sites na internet (HTTP)
alvo = "google.com" 
porta = 80

# [CONCEITO] — Criamos o objeto 'socket'. 
# AF_INET: Dizemos que usaremos endereços IPv4 (ex: 142.250.191.46)
# SOCK_STREAM: Dizemos que usaremos o protocolo TCP (o mais comum e confiável)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# [ATENÇÃO] — O método connect_ex tenta a conexão e nos dá um código numérico.
# Usamos connect_ex em vez de connect porque ele não interrompe o script se falhar.
# Se o resultado for 0, a conexão foi aceita (porta ABERTA).
resultado = cliente.connect_ex((alvo, porta))

if resultado == 0:
    print(f"Porta {porta} está ABERTA no alvo {alvo}!")
else:
    print(f"Porta {porta} está FECHADA ou inacessível.")

# [REPLICAR] — Sempre feche o socket para não deixar "fios soltos" no seu sistema.
cliente.close()
