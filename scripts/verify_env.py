import subprocess
import platform

print("Python:", platform.python_version())
subprocess.call("nvcc --version", shell=True)
subprocess.call("python -m pip --version", shell=True)
