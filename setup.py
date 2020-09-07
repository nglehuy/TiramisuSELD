# Copyright 2020 Huy Le Nguyen (@usimarit)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "tiramisu-asr>=0.1.9",
    "tensorflow>=2.3.0",
    "tensorflow-addons>=0.10.0",
    "setuptools>=47.1.1",
    "librosa>=0.7.2",
    "soundfile>=0.10.3",
    "PyYAML>=5.3.1",
    "matplotlib>=3.2.1",
    "numpy>=1.18.5,<1.19.0",
    "sox>=1.3.7",
    "nltk>=3.5",
    "numba==0.49.1",
    "tqdm>=4.47.0",
    "colorama>=0.4.3",
    "nlpaug>=0.0.14"
]

setuptools.setup(
    name="tiramisu-asr",
    version="0.0.1",
    author="Huy Le Nguyen, Huy Phan",
    author_email="nlhuy.cs.16@gmail.com",
    description="Speech Event Localization and Detection using Tensorflow 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usimarit/TiramisuSELD",
    packages=setuptools.find_packages(include=["tiramisu_seld*"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache-2.0 License",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)
