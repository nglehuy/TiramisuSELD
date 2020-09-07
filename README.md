<h1 align="center">
<p>TiramisuSELD :cake:</p>
<p align="center">
<a href="https://github.com/usimarit/TiramisuSELD/blob/master/LICENSE">
  <img alt="GitHub" src="https://img.shields.io/github/license/usimarit/TiramisuSELD?style=for-the-badge&logo=apache">
</a>
<img alt="python" src="https://img.shields.io/badge/python-%3E%3D3.6-blue?style=for-the-badge&logo=python">
<img alt="tensorflow" src="https://img.shields.io/badge/tensorflow-%3E%3D2.3.0-orange?style=for-the-badge&logo=tensorflow">
<img alt="ubuntu" src="https://img.shields.io/badge/ubuntu-%3E%3D18.04-blueviolet?style=for-the-badge&logo=ubuntu">
</p>
</h1>
<h2 align="center">
<p>Sound Event Localization and Detection in Tensorflow 2</p>
</h2>

<p align="center">
TiramisuSELD implements some speech event localization and detection architectures.
</p>

## Requirements

- Python 3.6+
- Tensorflow 2.2+: `pip install tensorflow`

## Setup Environment and Datasets

Install tensorflow: `pip3 install tensorflow` or `pip3 install tf-nightly` (for using tflite)

Install packages: `python3 setup.py install`

- To enable XLA, run `TF_XLA_FLAGS=--tf_xla_auto_jit=2 $python_train_script`

Clean up: `python3 setup.py clean --all` (this will remove `/build` contents)

## Training & Testing

**Example YAML Config Structure**

```yaml
speech_config: ...
model_config: ...
decoder_config: ...
learning_config:
  augmentations: ...
  dataset_config:
    train_paths: ...
    eval_paths: ...
    test_paths: ...
    tfrecords_dir: ...
  optimizer_config: ...
  running_config:
    batch_size: 8
    num_epochs: 20
    outdir: ...
    log_interval_steps: 500
```

See [examples](./examples/) for some predefined ASR models.

## References & Credits

1. [https://github.com/pquochuy/dcase2020-seld](https://github.com/pquochuy/dcase2020-seld)
