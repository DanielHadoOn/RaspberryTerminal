import os
import dialogs
# rm -a = remove tudo do diretorio
# rm -e .ext = remove extensao indicada
# rm arquivo = remove arquivo especifico

# _Path = self.path_root + "/" + "/".join(cmd[1:])
def Remove(self, cmd):
	try:
		if cmd[1] == '-a':
			for _arq in os.listdir(os.getcwd()):
				if os.path.isfile(_arq):
					os.remove(_arq)
					print " %s removido com sucesso!"%_arq

		elif cmd[1] == '-e': # Implementar exclusao de extensao
"""

		elif self.cmd[7:9] == '-e':
			EXT = '*.'+self.cmd[10:]
			for arquivo in glob.glob(EXT):
				os.remove(arquivo)
				print "%s removido com sucesso"%arquivo
"""
		else:
			if os.path.isfile(cmd[1]):
				print cmd[1]
				os.remove(cmd[1])
			else:
				print dialogs.Err2_Arq
	except:
		print dialogs.Err2_Arq

def Copy(self): # Implementar copia
	pass

"""
def MULTICOPY(self):
	arquivos_diretorio = glob.glob('*.*')
	for arquivos in range(len(arquivos_diretorio)):
		shutil.copy2(arquivos_diretorio[arquivos], '%s/%s'%(self.cmd[10:],arquivos_diretorio[arquivos]))
		print "%s copiado com sucesso para [%s]"%(arquivos_diretorio[arquivos],self.cmd[10:])
		
def COPY(self):
	COPY = self.cmd.split(' ')
	caminho1 = COPY[1]
	caminho2 = COPY[2]
	try:
		if os.path.isfile(caminho1):
			shutil.copy2(caminho1,caminho2)
			print "%s copiado com sucesso para %s"%(caminho1,caminho2)
	except:
		print 'Arquivo nao encontrado'

"""