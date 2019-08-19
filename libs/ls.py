import os
import glob
def Ls(cmd):
# Comando para listar arquivos e pastas
	try: # Executa caso seja repassados parametros
		if cmd[1] == '-e':
		# -e para determinar extensao do arquivo
			try:
				for arq in glob.glob(('*.' + cmd[2])):
					#print '\033[32m'+ arq
					print arq
			except:
				print " Extensao incorreta! "
		else:
			if os.path.exists(cmd[1]):
			# Caso a entrada seja um diretorio
			# Lista o conteudo deste diretorio
				for arq in os.listdir(cmd[1]):
					if os.path.isfile(arq):
					# Lista apenas arquivos
						#print '\033[32m'+ arq
						print arq
					else:
					# Lista apenas diretorios
						#print '\033[37m'+ arq
						print arq
	except:
	# Caso nao sejam repassados parametros
	# Lista apenas conteudos do diretorio atual
		for arq in os.listdir(os.getcwd()):
			if os.path.isfile(arq):
				#print '\033[32m'+ arq
				print arq
			else:
				#print '\033[37m'+ arq
				print arq