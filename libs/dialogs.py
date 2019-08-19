def Man(cmd):
	Man_Cmmd = {
	'cd':cd, 'rmdir':rmdir,
	'delete':delete,'rm':delete,
	'del':delete,'remove':delete,
	'cls':clear,'clear':clear,
	'copy':copy,'dict':dicti,
	'history':history,'ipview':ipview,
	'ls':ls,'mkdir':mkdir,
	'multicopy':multicopy,'pwd':pwd,
	'user':user,'view':view,'cript':cript
	}
	if cmd in Man_Cmmd:
		print Man_Cmmd[cmd]
	else:
		print Err6_Com

##################################################################################	
Err1_Sys = ' ERRO! Encerrando...'
Err2_Arq = ' ERRO! Arquivo nao encontrado '
Err3_Dir = ' ERRO! Diretorio nao encotnrado '
Err4_Dir = ' ERRO! Diretorio existente '
Err5_Dir = ' ERRO! Diretorio inexistente '
Err6_Com = ' ERRO! Comando nao encontrado '

cd = """ 

	Comando para entrar em um diretorio

	cd [diretorio] - Exemplos:

	-$ cd ..
	-$ cd /home/imagens

	"""

clear = """

	Comando para limpara a tela

	"""

copy = """

	Comando para copiar um arquivo de um diretorio para outro

	copy [caminho][arquivo] [destino][arquivo] - Exemplos:

	[Quando o arquivo nao se encontra no diretorio atual]:
	-$ copy /home/imagens/foto.jpg /home/fotos/foto.jpg

	[Quando o arquivo se encontra no diretorio atual]:
	-$ copy foto.jpg Imagens/fotos/foto.jpg

	"""

delete = """

	Comando para apaga arquivos

	delete [-all] [-e][extensao] [caminho][arquivo] - Exemplos:

	-$ delete -all - [Comando -all apaga todos os arquivos no diretorio]
	-$ delete -e txt - [Comando apaga apenas arquivos com extensao 'txt']
	-$ delete -e jpg - [Comando apaga apenas arquivos com extensao 'jpg']
	-$ delete /home/foto.jpg
	-$ delete aquivo.txt

	"""

dicti = """

	Comando de dicionario

	Traduz e exibe termos e significados

	-$ dict -gv - [Grava novos termos]
	-$ dict -p -tm significado ou termo - [Procura determinado]
	-$ dict -p -lt - [Lista todos os termos e significados]
	-$ dict -td texto.txt - [Traduz um arquivo de texto]

	"""

exit = """

	Encerra o programa

	"""

history = """

	Lista comandos digitados e os acessa conforme indice

	-$ h - [Lista todos os comando com indice a partir de 0 (zero)]
	-$ h ! - [Limpa todos os comandos]
	-$ h 2 - [Executa comando numero 2 da lista]

	"""

ipview = """

	Exibe as definiceos do endereco IP e demais informacoes

	"""

ls = """

	Lista arquivos do diretorio atual e encontra arquivos

	ls [-a] [-l][nome.extensao] - Exemplos:

	-$ ls

	foto.jpg
	arquivo.txt
	fotos

	-$ ls -l *.jpg [Lista todos os arquivos com extensao .jpg]
	-$ ls -l banco.txt [Econtra um arquivo]

	"""

mkdir = """

	Cria um diretorio

	mkdir [destino][diretorio] - Exemplos:

	[Criar diretorio 'fotos']:
	-$ mkdir /home/fotos
	-$ mkdir /home/arquivos/usuario/fotos

	[Ou para criar no diretorio atual]:
	-$ mkdir fotos/

	"""
multicopy = """

	Faz a copia de varios arquivos para um diretorio

	multicopy [destino] - Exemplos:
	-$ multicopy /home/fotos/

	"""

pwd = """

	Exibe o caminho atual nos diretorios

	"""

rmdir = """

	Comando remove um diretorio [Diretorio precisa estar vazio]

	rmdir [caminho][diretorio] - Exemplos:

	-$ rmdir /home/fotos
	-$ rmdir arquivos

	"""

user = """

	Altera o nome de usuario para o tradutor, apenas doze(12) caracteres

	user [nome de usuario] [senha] - Exemplos:

	-$ user daniel 472s21
	-$ user Alexandre 472s21

	"""

view = """

	Vizualiza ou cria arquivo de texto

	view [-r] [-w] - Exemplos:

	[Para vizualizar um arquivo de texto]:
	-$ view -r /home/arquivo.txt
	-$ view -r arquivo.txt

	[Para criar um arquivo de texto]:
	-$ view -w arquivo.txt

	"""

cript = """

	# Para Criptografar um Arquivo Digite a Linha de Comando:

	>> cript -c [nome_do_arquivo.extensao] [nome_de_saida] [tamanho_da_chave: 16 - 24 - 32]
	>> cript -c texto.txt texto_criptado 16

	# Para Decriptografar um Arquivo Digite a Linha de Comando:

	>> cript -d [nome_do_arquivo_encriptado]
	>> cript -d texto_criptado

	# Para Usar a Ferramente de Esteganografia com Arquivos Digite a Linha de Comando:

	>> cript -e [nome_da_imagem (apenas JPEG)] [nome_do_arquivo.extensao] [nome_de_saida]
	>> cript -e imagem arquivo.exe arquivo_saida

	# Para Usar a Ferramenta de Esteganografia com Textos Digite a Linha de Comando:

	>> cript -t [nome_da_imagem (apenas JPEG)] [nome_do_arquivo] [nome_de_saida]
	>> cript -t imagem texto1 imagem_de_saida

	"""