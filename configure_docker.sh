#!/bin/zsh

# This is configuring Docker to work with the ec2-user acoount
echo Configuring Docker... | cowsay
sudo usermod -a -G docker ec2-user && newgrp docker && sudo systemctl start docker.service && echo -e "\n${GREEN}[Configured Docker]${NC}\n"

echo -e "${GREEN}Initialization complete.${NC}" | cowsay
echo