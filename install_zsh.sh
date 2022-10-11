#!/bin/bash

# curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/install_zsh.sh | sh

# This is setting the color variables.
GREEN="\033[0;32m"
NC="\033[0m"

# This is installing the cowsay package and then echoing the message that it was installed.
echo -e "\n[Installing cowsay...]\n"
sudo yum install cowsay -y && echo -e "${GREEN}Installed Cowsay${NC}" | cowsay
echo

# This is installing the packages util-linux-user, git, and zsh.
# util-linux-user is needed for the chsh command.
for package in util-linux-user git zsh
do
        echo Installing ${package}... | cowsay
        echo
        sudo yum install -y $package && echo -e "\n${GREEN}[Installed ${package}]${NC}\n"
done

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

# This is changing the default shell to zsh.
sudo chsh -s $(which zsh) && sudo chsh -s $(which zsh) "$USER" && exec zsh -l
echo