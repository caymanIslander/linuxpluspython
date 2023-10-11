import subprocess

command = "neofetch"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#if the command is successfully executed
if result.returncode == 0:
    print("Command execution successful.")
    print("Output:\n", result.stdout)
else:
    print("Couldnt execute command")

