This repo demonstrates using the SM Python SDK without SM notebooks, SM Studio, or Jupyter.

# Install and configure the AWS CLI --> https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

# Install Anaconda --> https://www.anaconda.com/

# Create virtual environment and install packages
conda create -n sm-local python==3.9
conda activate sm-local
conda install pip pandas tensorflow sagemaker

# Execute SM training job
python sm-local.py
