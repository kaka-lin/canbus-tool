# CanBus Tool

This is canbus tool Implementation with ```PyQt5 + QML```. And it can be used in `Windows(kvaser)` or `Embedded Linux(SocketCAN)`.

## Usage

### 0. Setup your CAN

Please setup you CAN device.

```sh
# socketcan setup
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up
```

Through Socketcan, after finish setup you can, you will see `can0` show up by `ifconfig -a` as below:

![](images/can0.png)

### 1-1. Run with Docker (Recommend)

You can use the docker image that we already build, as below

```bash
$ docker pull kakalin/qt:5.12.0
```
> if you want to build if from scratch, please check [here](https://github.com/kaka-lin/qt-template/tree/master/docker)

And then running with docker:

```bash
$ ./run.sh
```

### 1-2. Run with local Qt

Please install Qt/QML on your local machine.

### 2. Install needed Python Packages

```bash
$ pip3 install -r requirements.txt
```
### 3. Running the program

```bash
$ python canbus_tool.py
```

Result as below:

<img src="images/canbus_tool_0.png">

<img src="images/canbus_tool_1.png">

## Configuration

If you using `python-can`, you can change configuration by edit `can.conf`.

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
    $ pyrcc5 -o src/qml.py src/resources/qml.qrc
    ```
