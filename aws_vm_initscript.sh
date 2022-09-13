#!/bin/sh
# The purpose of this program is to auto install packag$# on the aws virtual machine
#$packages=cowsay jq tmux

sudo amazon-linux-extras install epel

for package in cowsay git epel gcc zsh ohmyzsh zshrc jq tmux tldr
do
        sudo yum install -y $package
        echo $package installed... | cowsay
done

# Install Rust
echo Installing Rust... | cowsay
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > installrust.sh
chmod +x installrust.sh
./installrust.sh -y