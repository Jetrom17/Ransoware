import os
import binascii
import pyaes
import glob

key = b"1234567890123456"  # Chave de 16 bytes (128 bits)

# Defina o diretório onde estão os arquivos ".jet"
diretorio = "/home/jeiel/Área de Trabalho/YOUTUB3-main/BOB-Ransomware"

# Obtenha a lista de todos os arquivos ".jet" no diretório
arquivos_jet = glob.glob(os.path.join(diretorio, "*.jet"))

# Filtro
for arquivo in arquivos_jet:
    nome_original = os.path.splitext(arquivo)[0]
    
    with open(arquivo, "rb") as file:
        dados_codificados = file.read()
    
    # Remova o arquivo codificado
    os.remove(arquivo)
    
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Descriptografe os dados
    dados_decodificados = aes.decrypt(dados_codificados)

    with open(nome_original, "wb") as file:
        file.write(dados_decodificados)
