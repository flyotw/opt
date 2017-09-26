#!/bin/bash
for method in GET POST PUT DELETE TRACE CONNECT OPTIONS;
do
    printf "$method / HTTP/1.1\r\nHOST:scanme.nmap.org\r\n\r\n" | nc scanme.nmap.org 80
done