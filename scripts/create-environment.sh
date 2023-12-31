#!/bin/bash

source $(conda info --base)/etc/profile.d/conda.sh
conda deactivate

# Create conda ParlAI env 
#   - will create a conda env called <parlai>
conda create --force -n parlai python=3.10 -y
conda activate parlai

# Install torch
pip install torch --index-url https://download.pytorch.org/whl/cu118

# Install openai (for gpt3 prompting)
pip install openai

# ChatGPT stuff
pip install tiktoken

# Install transformers
pip install transformers scikit-learn

# Install Fairseq
#   It will have dependency conflicts with Mephisto and ParlAI
#   but the conflicts are not fatal.
# Expected error message:
#   ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
#   fairseq 0.12.2 requires hydra-core<1.1,>=1.0.7, but you have hydra-core 1.3.1 which is incompatible.
#   fairseq 0.12.2 requires omegaconf<2.1, but you have omegaconf 2.3.0 which is incompatible.
pip install fairseq==0.12.2

# Install ParlAI and Mephisto from source
cd packages

# Install ParlAI
cd ParlAI
pip install -e .
cd ..

# Install Search Engine dependencies
cd SearchEngine
pip install -r ./requirements.txt
cd ..

# Wrap-up
cd ..
conda deactivate
