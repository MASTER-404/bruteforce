import os, sys
os.system("git pull")
try:
    __import__("bruteforce")
except Exception as e:
    exit(str(e))
