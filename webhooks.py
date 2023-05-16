import subprocess
import sys


def git_pull():
    subprocess.check_call(['git', 'pull'])

try:
    git_pull()
except Exception as e:
    sys.stderr.write("Error pulling from git repo: " + str(e))
    sys.exit(1)
