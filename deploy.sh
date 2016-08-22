#!/bin/bash
foldername=`date +"%I:%M:%S"`
mkdir -p $foldername
cp /etc/apache2/mods-enabled/websocket.load $foldername
cd /home/var/
scons
scons install
cd /home/var/2
scons
scons install
service apache2 reload
