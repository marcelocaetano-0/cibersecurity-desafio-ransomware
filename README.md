# Desafio Cibersecurity Ransomware

### Ferramentas
- Kali Linux
- Nano
- Python

### Arquivos
- encrypter.py
Criptografa o arquivo utilizado para teste (teste.txt).
- decrypter.py
  Descriptografa o arquivo criptografado (teste.txt.ransomwaretroll)
- teste.txt
   Arquivo utilizado para teste.
- teste.txt.ransomwaretroll
   Arquivo criptografado.

### Observações

Alguns erros foram encontrados ao utilizar a versão do Kali Linux 

1. Ao executar o comando "#python encrypter" gerou o erro "ModuleNotFoundError: No module named 'pyaes'".
   Para solucionar foram necessários os seguintes passos:
     a. Atualização do sistema operacional
       apt-get update
     b. Instalação do modulo pyaes
       apt-get -y install python3-pyaes

2. A senha precisa ter exatamente 16 caracteres, caso contrário irá gerar o erro de "Invalid key size".
