## Overview

This is a simple python project for one of the interview exercises.  I'm following the directory layout
as described in the [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/structure/)


## Setup

### Prerequisites

You need python (version 2.x has been used here but 3 should work fine), virtualenv and pip. Make is also needed
to run some of the steps, however if you haven't got this then see Makefile for the raw python/pip commands to run instead.

On a stock MacBook virtualenv and pip aren't installed so you need to run the following as admin

```
sudo easy_install pip
sudo pip install virtualenv
```

For this point onwards you no longer need admin rights/shell and everything can be executed using a standard
user account which is just a Good Thing :)


### Virtualenv

To create a python virtual environment run the following commands

```
virtualenv matrix
. ./matrix/bin/activate
```

Now any packages installed with pip will only impact this virtual environment and won't pollute your system installed Python

### Install Packages

To install any required packages for the project running the following command

```
make init
```


## Tests

Currently these can be run as follows


```
make test
```



