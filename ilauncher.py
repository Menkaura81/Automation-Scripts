import subprocess
import sys


##################################################
# Configuracion para iniciar programas minimizados
##################################################
SW_MINIMIZE = 6
info = subprocess.STARTUPINFO()
info.dwFlags = subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = SW_MINIMIZE

######################
# Programas a ejecutar
######################
subprocess.Popen("C:\Program Files (x86)\Britton IT Ltd\CrewChiefV4\CrewChiefV4.exe", startupinfo=info)
subprocess.Popen("C:\Program Files\Simucube 2 True Drive\Simucube 2 True Drive Paddock.exe", startupinfo=info)
subprocess.Popen("C:\Program Files (x86)\SimHub\SimHubWPF.exe", startupinfo=info)
subprocess.Popen("C:\Program Files (x86)\Rhinode LLC\Trading Paints\Trading Paints.exe", startupinfo=info)
subprocess.Popen("C:\Program Files\Pimax\PimaxClient\pimaxui\PimaxClient.exe", startupinfo=info)
subprocess.Popen("H:\iRacing/ui\iRacingUI.exe")
subprocess.Popen("C:\Program Files\PimaxXR\companion.exe")
sys.exit(0)