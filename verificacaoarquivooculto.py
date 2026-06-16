import winreg
import os

try:
    chave = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run"
    )
    print("✔ Chave Run existe no Registro")
    i = 0
    while True:
        try:
            nome, valor, tipo = winreg.EnumValue(chave, i)

            print(f"Valor encontrado: {nome} -> {valor}")

            if os.path.exists(valor):
                if os.path.isfile(valor):
                    atributos = os.stat(valor).st_file_attributes
                    if atributos & 2:  # 2 = Hidden no Windows
                        print(f"⚠ Arquivo oculto detectado: {valor}")
            i += 1
        except OSError:
            break
    chave.Close()
except FileNotFoundError:
    print("✖ Chave Run não existe")