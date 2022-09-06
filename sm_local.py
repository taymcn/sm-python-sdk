import boto3
import sagemaker

sess = sagemaker.Session()
role = '<SM Execution Role ARN'

import os
import tensorflow.keras
import numpy as np
from keras.datasets import fashion_mnist

(x_train, y_train), (x_val, y_val) = fashion_mnist.load_data()

os.makedirs("./data", exist_ok = True)

np.savez('./data/training', image=x_train, label=y_train)
np.savez('./data/validation', image=x_val, label=y_val)

prefix = 'keras-fashion-mnist'

# Upload the training data set to 'keras-fashion-mnist/training'
training_input_path   = sess.upload_data('data/training.npz', key_prefix=prefix+'/training')

# Upload the validation data set to 'keras-fashion-mnist/validation'
validation_input_path = sess.upload_data('data/validation.npz', key_prefix=prefix+'/validation')

print(training_input_path)
print(validation_input_path)

from sagemaker.tensorflow import TensorFlow

tf_estimator = TensorFlow(entry_point='mnist_keras_tf.py',
                          role=role,
                          instance_count=1,
                          instance_type='ml.p3.2xlarge',   # Train on the local CPU ('local_gpu' if it has a GPU)
                          framework_version='1.15',
                          py_version='py3',
                          hyperparameters={'epochs': 1}
                         )

tf_estimator.fit({'training': training_input_path, 'validation': validation_input_path})

job_name = tf_estimator.latest_training_job.name
client = tf_estimator.sagemaker_session.sagemaker_client
description = client.describe_training_job(TrainingJobName=job_name)

# get s3 location of model artifacts
s3_model_artifacts = description['ModelArtifacts']['S3ModelArtifacts']

# download model artifacts to local machine
os.system(f'aws s3 cp {s3_model_artifacts} ./output/')