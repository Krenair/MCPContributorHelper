import socket
import time
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
f = s.makefile()
s.connect(('mcp.ocean-labs.de', 52506))
print '<<', f.readline().strip()

for command in open('cmds').read().splitlines():
    print '>>', command
    command_name = command.split(' ')[0]
    if command_name not in ['help', 'testcsv', 'scm', 'scf', 'ssm', 'ssf', 'fscm', 'fscf', 'fssm', 'fssf', 'pcf', 'pcm', 'psf', 'psm', 'fpcf', 'fpcm', 'fpsf', 'fpsm']:
        raise Error, 'I can\'t let you do that.'

    if command_name in ['getwhite']:
        linestoread = 1
    if command_name in ['help', 'testcsv', 'pcf', 'pcm', 'psf', 'psm']:
        linestoread = 2
    elif command_name in ['fpcf', 'fpcm', 'fpsf', 'fpsm']:
        linestoread = 3
    elif command_name in ['scm', 'scf', 'ssm', 'ssf']:
        linestoread = 4
    elif command_name in ['fscm', 'fscf', 'fssm', 'fssf']:
        linestoread = 5
    else:
        raise Error, 'Unknown command.'

    s.send(command + '\r\n')

    for i in range(0, linestoread):
        line = f.readline().strip()
        print '<<', line
        if line[1:] == 'It is illegal to use class names for fields or methods !':
            break

    time.sleep(2)

try:
    while True:
        sys.stdout.write(s.recv(1))
except KeyboardInterrupt:
    pass

s.close()
print ''
