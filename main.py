import os, sys

args = [sys.executable, '-c', 'pass']
newenv = os.environ.copy()

os.execve('/home/runner/UI-Maker-Process/proc', args, newenv);