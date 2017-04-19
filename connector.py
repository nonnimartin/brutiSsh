from pexpect import pxssh
import sys, getopt
import getpass

#get CLI args
cmd_args = sys.argv

#Go through CLI options, where argument value = cmd_args[opt + 1]
for opt in range(len(cmd_args)):
    if cmd_args[opt] == '-t':
        target   = cmd_args[opt + 1]
    if cmd_args[opt] == '-u':
        user     = cmd_args[opt + 1]
    if cmd_args[opt] == '-p':
        password = getpass.getpass()
    if cmd_args[opt] == '-c':
        #command will require quotes if has spaces
        command  = cmd_args[opt + 1]

def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    cmd_output = s.before

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print '[-] Error Connecting'
        exit(0)

s = connect(target, user, password)

send_command(s, command)
