#!/usr/bin/python3
from subprocess import call

call(["apt-get", "update", "-y"])
call(["apt-get", "upgrade", "-y"])
call(["apt-get", "dist-upgrade", "-y"])
call(["apt-get", "install", "bleachbit", "-y"])
call(["apt-get", "install", "proxychains", "-y"])
call(["apt-get", "install", "Preload", "-y"])
call(["apt-get", "install", "openssh-client", "-y"])
call(["apt-get", "install", "gitk", "-y"])
call(["apt-get", "install", "git-gui", "-y"])

