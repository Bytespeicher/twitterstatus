Hackerspace status bot
======================

Introduction
------------

A Twitter Bot that posts the current status of the HackerSpace

Installation
------------
In order to simply run the program, you can simply install dependencies by running

```shell
    git clone https://github.com/bytespeicher/twitterstatus.git .
    cp config.py.example config.py
    pip install -r requirements.txt
```

Building From Source
------------

Before you start, make sure you have Python and virtualenv installed and in 
your PATH.

Then execute the following commands on the command line:

```shell
    ENV_NAME=twitterstatus
    virtualenv $ENV_NAME
    cd $ENV_NAME
    source ./bin/activate
    pip install twitter
    git clone https://github.com/bytespeicher/twitterstatus.git .
    cp config.py.example config.py
```

After the virtual environment is set up, the Twitter library is installed and
the [twitterstatus](https://github.com/Bytespeicher/twitterstatus) repository is cloned.

You will need to generate Twitter OAuth keys and put them into `config.py`. Also you might want to check if CURRENT_STATUS is set 
to the path where your spaceapi `status.json` resides. When everything is set up
just run `twitterstatus.py` by the following command

```python
python3 twitterstatus.py
```

Contributions
------------

This is an open source project and contributions are always welcome

In order to contribute, refer to the Contribution Rules/Guidelines [here](https://github.com/Bytespeicher/Bytebot/blob/master/CONTRIBUTING.md)
