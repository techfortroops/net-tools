#!/bin/bash

sudo apt-get install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
cd /home/`whoami`/miniconda3/bin && source activate && cd -
conda update -n base -c defaults conda
conda env create -f environment.yml
conda activate techfortroops
conda install -c anaconda pip
pip3 install -r requirements.txt
python3 icmp.py
