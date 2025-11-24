import subprocess
import os

cwd = os.getcwd()
while (cmd := input("> ")) not in ("exit", "quit"):
    if cmd.startswith("cd "):
        path = cmd[3:].strip()
        try:
            cwd = os.path.abspath(os.path.join(cwd, path))
            os.chdir(cwd)  # обновляем для текущего процесса Python
        except Exception as e:
            print(f"cd error: {e}")
    else:
        result = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
