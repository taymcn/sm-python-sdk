This repo demonstrates using the SM Python SDK on Linux without SM notebooks, SM Studio, or Jupyter.

1. Install git
```
  sudo yum install git -y
```

2. Install and configure the AWS CLI
3. 
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

3. Install Anaconda
4. 
https://www.anaconda.com/

4. Create virtual environment and install packages
```
  conda create -n sm-local python==3.9
  conda activate sm-local
  pip install pandas tensorflow sagemaker
```

5. Clone repo
```
  git clone https://github.com/tmac8972/sm-local
```

6. Use SM Python SDK to create SM training job and download trained model locally
```
  python sm-local/sm_local.py
```

