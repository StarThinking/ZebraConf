#!/bin/bash

if [ $# -ne 1 ]; then echo wrong; exit -1; fi
disk=$1
apt-get update -y
apt-get -y install openjdk-8-jdk
#apt-get upgrade

sudo mkfs.ext4 /dev/$disk 
mkdir /root/vm_images
sudo mount /dev/$disk  /root/vm_images

apt install -y docker.io docker-compose

docker rm -f $(docker ps -aq); docker rmi -f $(docker images -q)
systemctl stop docker
rm -rf /var/lib/docker
mkdir /var/lib/docker
mount --rbind /root/vm_images /var/lib/docker
systemctl start docker
