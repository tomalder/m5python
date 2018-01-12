import subprocess

print('Running')

p = subprocess.Popen("N:\T.alder\My Documents\m5python\qt\pyuic5.bat -x design.ui -o mainDesign.py")

stdout,stderr = p.communicate()

print('Finished')