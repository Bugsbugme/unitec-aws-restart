#!/bin/bash
# The purpose of this program is to auto install package on the aws virtual machine
# To install, run this: sh -c "$(curl https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/aws_vm_initscript.sh)"

# Installing the cowsay package.
sudo yum install cowsay -y
echo Installed cowsay | cowsay

# Installing the epel repository.
sudo amazon-linux-extras install epel -y
echo Installed epel | cowsay

# This is a for loop that will install all the packages listed in the loop.
for package in git gcc zsh jq sl util-linux-user automake libevent-devel bison ncurses-devel
do
        sudo yum install -y $package
        echo Installed $package | cowsay
done

# This is installing rust.
echo Installing Rust... | cowsay
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > installrust.sh
chmod +x installrust.sh
./installrust.sh -y
echo Installed rust | cowsay

# This is installing broot.
mkdir $HOME/bin
curl https://dystroy.org/broot/download/x86_64-unknown-linux-gnu/broot > $HOME/bin/broot
chmod +x $HOME/bin/broot
broot --install
echo Installed broot | cowsay

# This is installing tmux.
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure
make
sudo make install
echo Installed tmux | cowsay

# This is installing ohmytmux.
cd $HOME
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
echo Installed ohmytmux | cowsay

# Installing tldr.
sudo pip3 install tldr && echo Installed tldr | cowsay

# This is installing ohmyzsh.
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && echo Installed ohmyzsh | cowsay

# Downloading the .zshrc file from the github repository and placing it in the home directory.
curl https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/data/.zshrc > $HOME/.zshrc && echo Retrieved .zshrc | cowsay

# Set ZSH_CUSTOM path
ZSH_CUSTOM=~/.oh-my-zsh/custom && echo ZSH_CUSTOM Path set | cowsay

# This is downloading the passion.zsh-theme file from the github repository and placing it in the
# ZSH_CUSTOM/themes/ directory.
curl https://raw.githubusercontent.com/ChesterYue/ohmyzsh-theme-passion/master/passion.zsh-theme > $ZSH_CUSTOM/themes/passion.zsh-theme && echo Retrieved ohmyzsh theme file | cowsay

# This is installing the zsh-autosuggestions plugin.
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions && echo Installed zsh-autosuggestions | cowsay

# This is changing the default shell to zsh.
sudo chsh -s $(which zsh) $(whoami) && exec zsh -l
