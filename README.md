This repo demonstrates using the SM Python SDK without SM notebooks, SM Studio, or Jupyter.

1. Install and configure the AWS CLI --> https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

2. Install Anaconda --> https://www.anaconda.com/

3. Create virtual environment and install packages
```
  conda create -n sm-local python==3.9
  conda activate sm-local
  conda install pip pandas tensorflow sagemaker
```

4. Execute SM training job:
```
  python sm-local.py
```
