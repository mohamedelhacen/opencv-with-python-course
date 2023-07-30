# OpenCV with Python

## Installation
### Create a venv
#### Windows
1. Method 1
```shell
python -m venv /path/to/new/<venv>
<venv>\Scripts\activate.bat
```
Replace `<venv>` with your venv name.
2. Method 2
```shell
pip install virtualenv
virtualenv <venv>
<venv>\Scripts\activate
```
To deactivate the venv:
```shell
deactivate
```
#### IOS and Linux
1. Method 1
```shell
python -m venv /path/to/new/<venv>
source <venv>/bin/activate
```
2. Method 2
```shell
pip install virtualenv
virtualenv <venv>
source <venv>/bin/activate
deactivate
```
### Install OpenCV
```shell
(venv) user~$ pip install opencv-python
```