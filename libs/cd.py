import os
import dialogs
# cmd[0]      cmd[1]
#   cd    /home/documentos
#   cd          ..

def Pwd(self):
	print " Ficticio: ",self.path_cmd
	print " Real: ",self.path_root

def Define_Paths(self):
	self.path_root = str(os.getcwd()) # Abre o diretorio do cmd.py
	self.user_usr = self.path_root + "/libs/getuser.usr"
	self.history = self.path_root + "/libs/history.hst"
	self.path_cmd = '/'
	#self.path_root += '/home'
	os.chdir(self.path_root)


def Cd(self, cmd):
	# Acessar diretorio anterior
	if cmd[1] == '..':
		#print cmd
		# /home/documentos/pasta
		# Separa cada palavra sem simbolos
		# ['home','documentos','pasta']
		_Path = self.split_geral.split(self.path_root)
		#print _Path
		# Retira espacos vazios
		_Path = filter(None, _Path)
		# Se o diretorio a ser acessado nao for o "raiz"
		if _Path[-1] != 'home':
			#print "Nao e raiz"
			# Retira ultimo elemento da lista
			# ['home','documentos']
			_Path.pop(-1)
			# Cria a string com o caminho completo
			# /home/documentos
			_Path_join = '/' + "/".join(_Path)
			# Transforma a string que eh exibida no
			# terminal em uma lista, retira espacos vazios
			_Path_cmd = filter(
				None,
				self.split_geral.split(self.path_cmd)
				)
			# Retira ultimo elemento da lista
			_Path_cmd.pop(-1)
			_Path_cmd = '/' + "/".join(_Path_cmd)

			#print _Path_cmd
			#print _Path_join

			try:
				# Se o acesso nao retornar erro
				if os.chdir(_Path_join) != 1:
					self.path_root = _Path_join
					self.path_cmd = _Path_cmd
			except:
				print dialogs.Err3_Dir

		else:
			print ""
	else:
	  # _Path = /home/../ + '/' + home/documentos/...
		_Path = self.path_root + '/' + "/".join(cmd[1:])
		print _Path
	  # Atualiza o caminho exibido na linha de comando
		_Path_cmd = self.path_cmd + "/".join(cmd[1:]) + '/'
		print _Path_cmd
		try:
			if os.chdir(_Path) != 1:
				# self.path_root = /home/../
				# _Path = /home/../home/documentos/...
				# Atualiza para o novo caminho acessado
				self.path_root = _Path
				self.path_cmd = _Path_cmd
				#print ' Diretorio acessado! '
		except:
			#print " Diretorio nao encontrado! "
			print dialogs.Err3_Dir