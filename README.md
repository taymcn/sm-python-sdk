This repo demonstrates basic use of the SageMaker Python SDK on Linux, without SM notebooks, SM Studio, or Jupyter.

1. Install git
```
sudo yum install git -y
```

2. Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

3. Install [Anaconda](https://www.anaconda.com/)

4. Create virtual environment and install packages
```
conda create -n sm-local python==3.9 -y
conda activate sm-local
pip install pandas tensorflow sagemaker
```

5. Clone this repo
```
git clone https://github.com/tmac8972/sm-python-sdk
```

6. Populate SM execution role in local copy of ```sm_training.py```

7. Use SM Python SDK to create SM training job and download trained model locally
```
cd sm-python-sdk
python sm_training.py
```

