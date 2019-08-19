import os
import dialogs

def Mkdir(self, cmd):
	try:
		_Path = self.path_root + '/' + "/".join(cmd[1:])
		if os.path.exists(_Path) == False:
			os.mkdir(_Path, 0755)
		else:
			print dialogs.Err4_Dir
	except:
		print dialogs.Err3_Dir

def Rmdir(self, cmd):
	try:
		_Path = self.path_root + '/' + "/".join(cmd[1:])
		if os.path.exists(_Path):
			os.rmdir(_Path)
		else:
			print dialogs.Err5_Dir
	except:
		print dialogs.Err3_Dir