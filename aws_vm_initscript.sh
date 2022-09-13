#!/bin/bash
# The purpose of this program is to auto install packag$# on the aws virtual machine
#$packages=cowsay jq tmux

for package in cowsay jq tmux
do
        sudo yum install -y $package
        echo $package installed... | cowsay
done

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh