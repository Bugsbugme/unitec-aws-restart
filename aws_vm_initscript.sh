#!/bin/bash
# The purpose of this program is to auto install packag$# on the aws virtual machine
$packages=cowsay jq tmux

for package in $packages
do
        sudo yum install -y $package
        echo $package installed... | cowsay
done