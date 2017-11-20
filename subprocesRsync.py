import subprocess
import sys

print '''Please provide full path of source and destination location\n
    Eg. moveit.py /source/dir/ /target/dir/'''

try:
    rsync = subprocess.check_output(['which', 'rsyncd']).split('\n')[0]
except:
    print "rsync command not found"
    sys.exit(1)

try:
    moveFrom = sys.argv[1]
    moveTo = sys.argv[2]
    subprocess.call([rsync, '--remove-source-files', '-avz', '--include', '*/', '--include', '*.png', '--exclude', '*', moveFrom, moveTo], shell=True)
except IndexError:
    print "Source or Destination Path is Missing"
    sys.exit(1)
