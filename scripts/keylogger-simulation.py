from datetime import datetime
from pathlib import Path

LOG = Path("keylog_simulado.txt")

def iniciar_keylogger():
    print("Keylogger SIMULADO (didático)")
    print("Digite algo. Para encerrar, digite ':q'.")

    with LOG.open("a", encoding="utf-8") as f:
        while True:
            texto = input("> ")
            if texto == ":q":
                print("Encerrado.")
                break
            timestamp = datetime.now().isoformat()
            f.write(f"{timestamp} - {texto}\n")

def simular_envio_email():
    print("\n[SIMULAÇÃO] Enviando log por e-mail...")
    print("Conteúdo enviado (simulado):")
    print(LOG.read_text())

if __name__ == "__main__":
    iniciar_keylogger()
    simular_envio_email()
