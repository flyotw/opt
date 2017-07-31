#!/usr/bin/python3
import os
from subprocess import call
call(["systemctl", "start", "postgresql"])
#call(["msfdb", "-h"])
#call(["msfdb", "init"])


#systemctl start postgresql
#msfdb init
