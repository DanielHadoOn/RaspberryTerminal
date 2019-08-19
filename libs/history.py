# history
# History(self, cmd, 1) Apenas salva os comandos
# History(self, cmd, 2) Exibe comandos
# History(self, cmd, 3) Executa comandos

def History(self, cmd, _type):
	if _type == 1: # Carrega a lista de comandos
		# Faz a varredura diretamente no arquivo sem abri-lo
		for line in open(self.history):
			self.hist_list.append(line.split("\n")[0])

	elif _type == 2: # Arquiva a lista de comandos
		COMMD = [
		'dir','pwd','ls','cd','rm',
		'clear','cript','ipview',
		'copy','dict','dir','man',
		'mkdir','rmdir','multicopy',
		'user','view','!','>>','del',
		'delete','remove','cls'
		]
		# Compara o comando com a lista e verifica se
		# eh um comando valido
		if cmd[0] in COMMD:
			self.hist_list.append(self.cmd)
			#self.hist_list.append(" ".join(map(str,cmd)))
			self.hist_list = list(set(self.hist_list))

			arq = open(self.history,'w')
			for Commd in self.hist_list:
				arq.write(Commd + "\n")
			arq.close()

	elif _type == 3: # Exibe e executa comandos
		try: # Caso haja argumentos para o comando
			if cmd[1] == "!":
				self.hist_list = []
				print " Historico de comandos limpo! "

			# Caso o tipo de entrada seja inteira, executa
			# [h 2] ou [h 5] - [history 2] ou [history 5]
			elif type(int(cmd[1])) == int:
				self.Loop_Commands(self.hist_list[int(cmd[1])])

		except: # Caso apenas h seja inserido, lista
			for num, comd in enumerate(self.hist_list):
				print " ", num, comd
