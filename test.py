from subprocess import run
from datetime import datetime

result = run('git status', capture_output=True)

print(datetime.now())

