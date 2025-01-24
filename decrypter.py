import os
import pyaes

## Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave de criptografia
key = b"cripransowaremarcelo"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo
os.remove(file_name)

## Salvar arquivo criptografado
new_file = "teste.txt"
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
