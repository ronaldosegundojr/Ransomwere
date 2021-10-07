import os, pyaes

# Localizando e lendo os dados do arquivo ou diretório
file_name = 'nomedoarquivo.txt.teste' #Arquivo ou diretório que será ser encriptado
file = open(file_name, 'rb') #Abrindo no modo leitura
file_data = file.read() #Ler os dados do arquivo
file.close()

# Criptografando os dados do arquivo ou diretório
chave = '0h2lK8I6Y39Y1T!%' #Chave aleatória da Criptografia com 16 caracteres, com 16 bites
aes = pyaes.AESModeOfOperationCTR(chave) #função que criptografa/descriptografa
encripta_dados = aes.decrypt(file_data) #descriptografando o arquivo

novo_nome_arquivo = 'concluido.txt' #Criar novo arquivo com a nova extensão
novo_arquivo = open(novo_nome_arquivo, 'wb') #Abrindo no modo escrita
novo_arquivo_data = file.write(encripta_dados) #substituindo os dados descriptados no novo arquivo
novo_arquivo.close()