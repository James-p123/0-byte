import subprocess
 
try:
    result = subprocess.run(['/path/to/command', 'arg1', 'arg2'], check=True)
except subprocess.CalledProcessError as e:
    print(f"命令执行失败: {e}")