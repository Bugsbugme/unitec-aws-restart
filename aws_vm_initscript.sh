#!/bin/bash
# The purpose of this program is to auto install package on the aws virtual machine
# To install, run this: curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/aws_vm_initscript.sh | sh && exec zsh -l

# Setting a green color variable.
GREEN="\033[0;32m" && clear

# Installing the cowsay package.
echo -e "${GREEN}Installing cowsay...\n"
sudo yum install cowsay -y && clear && echo Installed cowsay | cowsay

# Installing the epel repository.
echo Installing epel... | cowsay
echo
sudo amazon-linux-extras install epel && echo -e "${GREEN}Installed epel\n"

# This is a for loop that will install all the packages listed in the loop.
for package in git gcc zsh jq sl util-linux-user automake libevent-devel bison ncurses-devel
do
        echo Installing ${package}... | cowsay
        echo
        sudo yum install -y $package && echo -e "${GREEN}Installed ${package}\n"
done

# This is installing ohmyzsh.
echo Installing ohmyzsh... | cowsay
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && echo -e "${GREEN}Installed ohmyzsh\n"

# Downloading the .zshrc file from the github repository and placing it in the home directory.
echo Fetching zshrc config... | cowsay
curl https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/data/.zshrc > $HOME/.zshrc && echo -e "${GREEN}Retreived zshrc config\n"

# Set ZSH_CUSTOM path
ZSH_CUSTOM=~/.oh-my-zsh/custom && echo -e "${GREEN}Set ZSH_CUSTOM path\n"

# This is downloading a ohmyzsh theme file from the github repository and placing it in the
# ZSH_CUSTOM/themes/ directory.
echo Fetching ohmyzsh theme... | cowsay
curl https://raw.githubusercontent.com/ChesterYue/ohmyzsh-theme-passion/master/passion.zsh-theme > $ZSH_CUSTOM/themes/passion.zsh-theme && echo -e "${GREEN}Retreived ohmyzsh theme\n"

# This is installing the zsh-autosuggestions plugin.
echo Installing zsh-autosuggestions... | cowsay
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions && echo -e "${GREEN}Installed zsh-autosuggestions\n"

# This is changing the default shell to zsh.
sudo chsh -s $(which zsh) $(whoami)
echo

# Installing tldr.
echo Installing tldr... | cowsay
sudo pip3 install tldr && echo -e "${GREEN}Installed tldr\n"

# This is installing rust.
echo Installing rust... | cowsay
echo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > installrust.sh
chmod +x installrust.sh
./installrust.sh -y
echo -e "${GREEN}Installed rust\n"

# This is installing broot.
echo Installing broot... | cowsay
mkdir $HOME/bin
curl https://dystroy.org/broot/download/x86_64-unknown-linux-gnu/broot > $HOME/bin/broot
chmod +x $HOME/bin/broot
broot --install
echo -e "${GREEN}Installed broot\n"

# This is installing tmux.
echo Installing tmux... | cowsay
echo
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure
make
sudo make install
echo -e "${GREEN}Installed tmux\n"

# This is installing ohmytmux.
cd $HOME
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
echo -e "${GREEN}Installed ohmytmux\n"

echo -e "${GREEN}Initialization complete." | cowsay