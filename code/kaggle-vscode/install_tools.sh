#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Installing Python3..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
else
    echo "Python3 is already installed."
fi

# Check if Jupyter is installed
if ! command -v jupyter &> /dev/null
then
    echo "Jupyter not found. Installing Jupyter..."
    pip3 install jupyter
else
    echo "Jupyter is already installed."
fi

# Check if the Python VSCode extension is installed
if [ ! -d "$HOME/.vscode-server/extensions/ms-python.python-*" ]; then
    echo "VSCode Python extension not found. Installing..."
    code --install-extension ms-python.python
else
    echo "VSCode Python extension is already installed."
fi

# Check if the Jupyter VSCode extension is installed
if [ ! -d "$HOME/.vscode-server/extensions/ms-toolsai.jupyter-*" ]; then
    echo "VSCode Jupyter extension not found. Installing..."
    code --install-extension ms-toolsai.jupyter
else
    echo "VSCode Jupyter extension is already installed."
fi

# Check if the GitHub Copilot Chat extension is installed
if [ ! -d "$HOME/.vscode-server/extensions/github.copilot-chat-*" ]; then
    echo "VSCode GitHub Copilot Chat extension not found. Installing..."
    code --install-extension github.copilot-chat
else
    echo "VSCode GitHub Copilot Chat extension is already installed."
fi

# Install nvidia-utils-515
echo "Installing nvidia-utils-515..."
sudo apt-get update
sudo apt-get install -y nvidia-utils-515
