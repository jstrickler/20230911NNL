from subprocess import run, CalledProcessError, PIPE
from shlex import split   # split on space but preserve *quoted* space

cmd = 'spam -d red "light blue"   "layer cake"'
cmd_words = split(cmd)
print(f"cmd_words: {cmd_words}")

cmd = 'netstat -n'

cmd_words = split(cmd)

process = run(cmd_words, stdout=PIPE)

output = process.stdout.decode().splitlines()

for raw_line in output:
    fields = raw_line.split()
    if not fields:
        continue
    if fields[0]== 'TCP':
        local, foreign, state = fields[1:]
        if state == 'ESTABLISHED':
            print(local, foreign)
    

