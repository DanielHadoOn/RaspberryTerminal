# -*- coding: utf-8 -*-
# ESTE CODIGO SERVIRA COMO INTERFACE PARA MANIPULAR ALGUMAS FUNCOES ESPECIFICAS NO RASPBERRY PI
# IMITA O FUNCIONAMENTO DE UM INTERPRETADOR DE COMANDOS TIPO UNIX
# REALIZARA TAREFAS DENTRO DO DISPOSITIVO RASPBERRY PI ZERO W

# ABRE NA RAIZ DO DISPOSITIVO
# SISTEMA OPERACIONAL RASPIAN LITE
# ACESSO POR SSH

# CRIAR ACESSO POR REDE, TRANSFERENCIA DE ARQUIVOS, DO TCC DO SOLON

# 

import os			# Modulo para manipular o SO
import re 			# Modulo para trabalhar com strings
import glob			# Modulo para trabalhar com arquivos em diretorios
from libs import *  # [libs] é o diretorio dos modulos chamados, como: cd,ls,getusr..
#########################################################################################################
class Sys_Prompt: # Classe principal do programa
	def __init__(self): # Metodo de inicio da Classe
		self.cmd = '' # Prompt de comando, recebe os comandos
		self.user = 'HadoOn42' # Nome de usuario
		self.path_cmd = '' # Caminho exibido na linha de comando
		self.path_root = ''
		self.hist_list = []
		self.split_geral = re.compile('[\n /,]') # retira simbolos

	def Loop_Commands(self, _cmd): # Executa os comandos repassados
		# Se nenhum comando for repassado
		# de modulos externos
		if _cmd == None:
			cmd = self.split_geral.split(self.cmd)
		# Se for repassado comandos externamente
		else:
			cmd = self.split_geral.split(_cmd)
		try:
		#if 1:
			# Armazena os comandos digitados
			history.History(self, cmd, 2)

			if cmd[0] == 'cd':
				cd.Cd(self, cmd)
			elif cmd[0] in ['history','h']:
				history.History(self, cmd, 3)
			elif cmd[0] == 'ls':
				ls.Ls(cmd)
			elif cmd[0] == 'man':
				dialogs.Man(cmd[1])
			elif cmd[0] == 'mkdir':
				pathdir.Mkdir(self, cmd)
			elif cmd[0] == 'pwd':
				cd.Pwd(self)
			elif cmd[0] in ['rm','remove','delete','del']:
				pathfile.Remove(self, cmd)
			elif cmd[0] == 'rmdir':
				pathdir.Rmdir(self, cmd)
			elif cmd[0] in ['clear','cls']:
				os.system('clear')
		except:
			print " "

	def Boot(self):
 	# Faz carregamento previo dos arquvivos, diretorios, variaveis
 	# Determina caminhos, le arquivos para o sistema
 		cd.Define_Paths(self)
 		history.History(self, "", 1)
 		return 0

#########################################################################################################
Exc = Sys_Prompt() # Inicia a classe do programa
if Exc.Boot() == 0: # Se o Boot retornar valor positivo
	while Exc.cmd not in ['exit','poweroff','quit']:
		Exc.cmd = str(raw_input(Exc.user + "@" + Exc.path_cmd + "-$ "))
		Exc.Loop_Commands(Exc.cmd)


"""
		elif self.cmd[:5] == 'image':
			if self.cmd[6:8] == '-o':
				PyPicture(self.cmd[9:]

		elif self.cmd[:5] == 'cript':
			if self.cmd[6:8] == '-c':
				Criptografar(self)
			elif self.cmd[6:8] == '-d':
				Decriptografar(self)
			elif self.cmd[6:8] == '-e':
				Esteganografia_Arquivo(self)
			elif self.cmd[6:8] == '-t':
				Esteganografia_Texto(self)


def Gera_Chave(tamanho):
    caracters = '0123456789abcdefghijlmnopqrstuwvxzABCDEFGHIJKLMNO\
PQRSTUVWXYZ\:<>/}{[]+=_-@#$%&*!^~'
    chave = ''
    for char in xrange(tamanho):
        chave += choice(caracters)
    return  chave

def Armazena_Chave(CH, nome_in, nome_out):
	nome_out += '.pass'
	Pacote_Chave = open(nome_out,'w')
	chave_b64 = base64.b64encode(CH)
	Pacote_Chave.write(nome_in + ' ' + chave_b64)
	Pacote_Chave.close()

def cifra_bloco(s, block_size):
     return s.ljust(len(s) + block_size - (len(s) % block_size))
##################################################################################################

def Criptografar(self):
	Nome_Arq = self.cmd.split(' ') #Quebra o conteudo da variavel
	nome_in = Nome_Arq[2] #Nome de Arquivo de entrada
	nome_out = Nome_Arq[3] #Nome de Arquivo de saida
	tamanho = int(Nome_Arq[4]) #Tamanho referencia para criacao da chave
	if os.path.isfile(nome_in):#Verifica se o arquivo de entrada existe
		if tamanho == 16 or tamanho == 24 or tamanho == 32:
			CH = Gera_Chave(tamanho)#Funcao que gera a chave de acordo com o tamanho escolhido
			Armazena_Chave(CH,nome_in,nome_out) #Armazena a chave e o nome do arquivo original
			nome_out += '.kpt' #Cria o nome e extensao do arquivo criptografado

			Arq_Entrada = open(nome_in,'rb') #Abre o arquivo de entrada em modo de leitura binaria
			Arq_Saida = open(nome_out,'wb') #Cria o arquivo de saida em modo de escrita binaria

			Cifra_AES = AES.new(CH, AES.MODE_ECB) #cria a criptografia
			Pacote = Arq_Entrada.readlines() #le todas as linhas do arquivo de entrada
			Cifra_Cripto = ''#inicia a variavel vazia para receber linha apos linha criptografada
			for bit in range(0, len(Pacote)): #percorre as linhas do Arquivo
				#Cifra_Cripto += Pacote[bit]
				Pacote_linhas = Pacote[bit] 
				Cifra_Cripto += Pacote_linhas #armazena linha por linha e monta na variavel Cifra_Cripto
			Cripto_Pacote = Cifra_AES.encrypt(cifra_bloco(Cifra_Cripto, AES.block_size)) #Criptografa o pacote inteiro
			Arq_Saida.write(Cripto_Pacote) #Grava a criptografia no arquivo de saida
			Arq_Entrada.close() 
			Arq_Saida.close()# Fecha os arquivos
			print "\n\t### Arquivo Criptografado com Sucesso! ###\n"

def Decriptografar(self):
	Nome_Arq = self.cmd.split(' ')
	nome_in = Nome_Arq[2]
	Arq_Cripto = nome_in + '.kpt'
	Arq_Chave = nome_in + '.pass'
	if os.path.isfile(Arq_Cripto):
		if os.path.isfile(Arq_Chave):
			Arquivo_PASS = open(Arq_Chave,'r')
			Linha = Arquivo_PASS.readline().split(' ')
			Nome_Arq_in = Linha[0]
			CH = Linha[1]
			Chave_Cript = base64.b64decode(CH)
			Arquivo_PASS.close()

			Cifra_AES = AES.new(Chave_Cript, AES.MODE_ECB)

			KPT = open(Arq_Cripto,'rb')
			Arq_Decripto = open(Nome_Arq_in,'wb')

			Decriptado = ''
			Pacote = KPT.readlines()
			for bit in range(0, len(Pacote)):
				Pacote_linhas = Pacote[bit]
				Decriptado += Pacote_linhas
			Pacote_Decriptado = Cifra_AES.decrypt(Decriptado).strip()
			Arq_Decripto.write(Pacote_Decriptado)
			Arq_Decripto.close()
			KPT.close()
			print "\n\t### Arquivo Decriptografado com Sucesso! ###\n"
"""