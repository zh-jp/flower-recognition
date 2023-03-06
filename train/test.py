import tensorflow as tf
tensorflow_version=tf.__version__
gpu_available=tf.test.is_gpu_available()
print("tensorflowversion:",tensorflow_version,"\tGPU available:",gpu_available)
