# CanBus Tool - Backend (Python Ver.)

## Usage

### 1. Install needed Python Packages

```bash
$ pip3 install -r requirements.txt
```
### 2. Running the program

```bash
$ python canbus_tool.py
```

When you start sending/receiving can data would be like this:

<img src="../images/canbus_tool_1.png">

## Configuration

You can change configuration by edit `can.conf`.

The configuration files sets the default interface and channel, as below:

```
[default]
interface = <the name of the interface to use>
channel = <the channel to use by default>
bitrate = <the bitrate in bits/s to use by default>
```

Other detail informtation please see [here](https://python-can.readthedocs.io/en/stable/configuration.html).

## Packaging

if you want to packing Python programs into ```stand-alone executables```

1. Converting ```*.qrc``` (a collection of resource) files into ```*.py``` (Python source) file

    ```bash
    $ pyrcc5 -o src/qml.py ../frontend/qml.qrc
    ```

## TroubleShoot

### libQt5MultimediaQuick.so.5: cannot open shared object file: No such file or directory

Solution:

```bash
$ cp qml-shared-library/* <YOUR_PYTHON_PATH>/site-packages/PyQt5/Qt5/lib

# example
$ cp qml-shared-library/* /home/alioth/opt/miniconda3/envs/py36/lib/python3.6/site-packages/PyQt5/Qt5/lib
```

- [Reference](https://stackoverflow.com/questions/61426174/libqt5multimediaquick-so-5-cannot-open-shared-object-file-no-such-file-or-dire
)
