This repo demonstrates using the SageMaker Python SDK on Linux, without SM notebooks, SM Studio, or Jupyter.

1. Install git
```
sudo yum install git -y
```

2. Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

3. Install [Anaconda](https://www.anaconda.com/)

4. Create virtual environment, install packages, and clone this repo
```
conda create -n sm-python-sdk python==3.9 -y
conda activate sm-python-sdk
pip install pandas tensorflow sagemaker
git clone https://github.com/tmac8972/sm-python-sdk
cd sm-python-sdk
```

5. Populate [SM execution role](https://github.com/tmac8972/sm-python-sdk/blob/65e2a1640fa4b53d37e3ecc245a3e829d28bf79d/sm_training.py#L9) in local copy of ```sm_training.py```

6. Use SM Python SDK to create SM training job
```
python sm_training.py
```

