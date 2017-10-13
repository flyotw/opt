#!/usr/bin/python3
from subprocess import call

#install docker:  https://termilus.com/blog/2016/11/04/how-to-install-docker-on-kali-linux/
call(["echo", "deb http://http.debian.net/debian wheezy-backports main", ">", "/etc/apt/sources.list.d/backports.list"])
call(["apt-get", "update"])
call(["apt-get", "install", "apt-transport-https", "-y"])
call(["apt-get", "install", "ca-certificates", "-y"])
call(["apt-key", "adv", "--keyserver", "hkp://p80.pool.sks-keyservers.net:80", "--recv-keys", "58118E89F3A912897C070ADBF76221572C52609D"])
call(["echo", "deb http://http.debian.net/debian wheezy-backports main", ">", "/etc/apt/sources.list.d/docker.list"])
call(["apt-get", "update"])
call(["apt-get", "install", "docker-engine", "-y"])

call(["apt-get", "update", "-y"])
call(["apt-get", "upgrade", "-y"])
call(["apt-get", "dist-upgrade", "-y"])
call(["apt-get", "install", "bleachbit", "-y"])
call(["apt-get", "install", "proxychains", "-y"])
call(["apt-get", "install", "preload", "-y"])
call(["apt-get", "install", "openssh-client", "-y"])
call(["apt-get", "install", "openssh-server", "-y"])
call(["apt-get", "install", "gitk", "-y"])
call(["apt-get", "install", "git-gui", "-y"])
call(["apt-get", "install", "chkrootkit", "-y"])
#call(["apt-get", "install", "virtualbox", "-y"])
call(["apt-get", "install", "kali-linux-web", "-y"])
call(["apt-get", "install", "gufw", "-y"])
call(["apt", "autoremove", "-y"])

call(["chkrootkit"])
call(["gufw"])

#set service start procs
call(["update-rc.d", "apache2", "enable"])
call(["update-rc.d", "mysql", "enable"])
call(["update-rc.d", "postgresql", "enable"])
call(["update-rc.d", "docker", "enable"])

#call(["service", "apache2", "start"])
call(["service", "postgresql", "start"])
call(["service", "mysql", "start"])
call(["service", "docker", "start"])

call(["docker", "run", "hello-world"])
