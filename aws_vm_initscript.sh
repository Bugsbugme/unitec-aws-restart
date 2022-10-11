#!/bin/bash
# The purpose of this program is to auto install package on the aws virtual machine
# To install, run this: 
# curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/aws_vm_initscript.sh | sh && exec zsh -l

# This is setting the color variables.
GREEN="\033[0;32m"
NC="\033[0m"

# This is installing the cowsay package.
echo -e "\n[Installing Cowsay...]\n"
sudo yum install cowsay -y && echo -e "${GREEN}Installed Cowsay${NC}" | cowsay
echo

# This is installing the epel repository.
echo Installing the Epel Repository... | cowsay
echo
sudo amazon-linux-extras install epel && echo -e "\n${GREEN}[Installed the Epel Repository]${NC}\n"

# This is a for loop that will install all the packages listed in the loop.
# util-linux-user is needed for the chsh command.
# gcc is needed for C compiling.
# jq is a lightweight and flexible command-line JSON processor
# automake and bison are needed to build Tmux
for package in util-linux-user zsh git gcc jq automake libevent-devel ncurses-devel bison docker
do
        echo Installing ${package}... | cowsay
        echo
        sudo yum install -y $package && echo -e "\n${GREEN}[Installed ${package}]${NC}\n"
done

# This is installing tmux.
echo Installing tmux... | cowsay
echo
git clone https://github.com/tmux/tmux.git $HOME/bin/tmux
cd $HOME/bin/tmux
sh autogen.sh
./configure
make
sudo make install && echo -e "\n${GREEN}[Installed tmux]${NC}\n"
cd $HOME

# This is installing ohmytmux.
echo Installing ohmytmux... | cowsay
echo
git clone https://github.com/gpakosz/.tmux.git $HOME/bin/oh-my-tmux
ln -s -f $HOME/bin/oh-my-tmux/.tmux.conf ~/.tmux.conf
cp $HOME/bin/oh-my-tmux/.tmux.conf.local ~/.tmux.conf.local && echo -e "\n${GREEN}[Installed Oh My Tmux]${NC}\n"

# This is installing broot.
echo Installing Broot... | cowsay
echo
curl -s https://dystroy.org/broot/download/x86_64-unknown-linux-gnu/broot > $HOME/bin/broot && chmod +x $HOME/bin/broot
broot --install && echo -e "\n${GREEN}[Installed Broot]${NC}\n"

# This is installing the tldr package.
echo Installing tldr... | cowsay
echo
sudo pip3 install tldr && echo -e "\n${GREEN}[Installed tldr]${NC}\n"

# This is installing ohmyzsh.
echo Installing Oh My Zsh... | cowsay
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && echo -e "\n${GREEN}[Installed Oh My Zsh]${NC}\n"

# Downloading the .zshrc file from the github repository and placing it in the home directory.
echo Fetching zshrc config... | cowsay
curl https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/data/.zshrc > $HOME/.zshrc && echo -e "\n${GREEN}[Retreived zshrc config]${NC}\n"

# This is downloading an ohmyzsh theme file from the github repository and placing it in the ZSH_CUSTOM/themes/ directory.
echo Fetching Oh My Zsh theme... | cowsay
echo
ZSH_CUSTOM=~/.oh-my-zsh/custom
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1 && echo -e "\n${GREEN}[Retreived ohmyzsh theme]${NC}\n"
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# This is installing the zsh-autosuggestions plugin.
echo Installing zsh-autosuggestions... | cowsay
echo
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions && echo -e "\n${GREEN}[Installed zsh-autosuggestions]${NC}\n"

# This is installing the zsh-syntax-highlighting plugin.
echo Installing zsh-syntax-highlighting... | cowsay
echo
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting && echo -e "\n${GREEN}[Installed zsh-syntax-highlighting]${NC}\n"

# This is installing rust.
# echo Installing rust... | cowsay
# echo
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > installrust.sh
# chmod +x installrust.sh
# ./installrust.sh -y && echo -e "\n${GREEN}[Installed rust]${NC}\n"

# This is changing the default shell to zsh.
echo Changing default Shell to ZShell... | cowsay
sudo chsh -s $(which zsh) && sudo chsh -s $(which zsh) "$USER"
echo

# This is configuring Docker to work with the ec2-user acoount
echo Configuring Docker... | cowsay
sudo usermod -a -G docker ec2-user | sh && newgrp docker | sh && sudo systemctl start docker.service | sh && echo -e "\n${GREEN}[Configured Docker]${NC}\n"

echo -e "${GREEN}Initialization complete.${NC}" | cowsay
echo

# This is using an external script to install ZShell, Oh My Zsh and some other ZShell plugins
# echo Installing ZShell... | cowsay
# echo
# curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/install_zsh.sh | sh && echo -e "\n${GREEN}[Installed ZShell]${NC}\n"

# This is configuring Docker to work with the ec2-user acoount
# echo Configuring Docker... | cowsay
# echo
# curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/configure_docker.sh | zsh && echo -e "\n${GREEN}[Configured Docker]${NC}\n"

# echo -e "${GREEN}Initialization complete.${NC}" | cowsay
# echo