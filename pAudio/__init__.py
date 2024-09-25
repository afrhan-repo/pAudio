import subprocess

try:
    check_pulseaudio_running = subprocess.run(['pulseaudio', '--check'], stdout=subprocess.PIPE,check=True)
except:
    print("Pulseaudio is not running,So starting it")
    subprocess.run(['pulseaudio', '--start',"--exit-idle-time=-1"])

__version__ = "0.2.0"
