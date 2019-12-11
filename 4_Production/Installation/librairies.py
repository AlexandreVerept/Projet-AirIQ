import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    
listLibrairies = ["schedule==0.6.0",
                  "tensorflow==1.14.0",
                  "matplotlib==3.1.1",
                  "numpy=1.17.3", 
                  "pandas==0.25.2",
                  "keras==2.2.4",
                  "pymysql==0.9.3",
                  "urllib3==1.24.2",
                  "json5==0.8.5"]

for lib in listLibrairies:
    install(lib)