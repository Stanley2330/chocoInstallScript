import subprocess
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def call_command(cmd):
    if is_admin():
        subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ' + cmd, shell=True)
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
