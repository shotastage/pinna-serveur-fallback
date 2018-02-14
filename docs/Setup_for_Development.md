# Setup for Development

This chapter will introduce about how to setup development environment on your computer.

## Required Tools

You have to install these tools in advance before starting your development.
Detail instruction is below chapter.

* [Anaconda](https://anaconda.org/anaconda/python) - Create and manage specific Python environment
* [Mirage](https://github.com/shotastage/mirage) - Extended Django admin CLI and manager
* [Pipenv](https://github.com/pypa/pipenv) - Advanced pip extended package manager
* [Yarn](https://yarnpkg.com/en/) - Extended NPM package manager

## Detail Description of Each Tools

### [Anaconda](https://anaconda.org/anaconda/python)

Anaconda is package of widely used softwares such as Python or R and these libraries.
You can create Python environment made separated from system installed Python.

### [Mirage](https://github.com/shotastage/mirage)

Mirage is super integrated manager and tools for Django. It provides many management console and Rails like
 shorten CLI.
Moreover, Mirage has environment manager that enables us to manage secret environment and it also provides
 advanced auto model generating system.

### [Pipenv](https://github.com/pypa/pipenv)

Pipenv is next-generation super advanced package manager for Python.
Recently, almost all Pythonista uses **pip** as a default Python package manager.
However, pip does not provide auto upgrading feature, and we hove to update installed package manually.
Pipenv provides auto package upgrading feature and locking required version feature.
Thus, we can manage packages more efficiently.

### [Yarn](https://yarnpkg.com/en/)

Yarn is FAST, RELIABLE, AND SECURE DEPENDENCY MANAGEMENT for Node.js
It provides extended npm features such as package version locking.

# Install requirements

First, you have to check your computer specification.
If you use macOS or Ubuntu, you can proceed this instruction. But, if the Windows, we currently don't support this platform.
If you completed platform checking, please check below minimum requirements.

### Minimum 

|     Heading      |            Contents           |
|:-----------------|:------------------------------|
| Operating System | macOS 10.13.3+  Ubuntu 16.04+ |
| CPU & RAM        | Newer x86 CPU ans 8 ~ 16GB    |
| Installation     | Homebrew or Linuxbrew, Node.js, Python3 |


## macOS

### 1. Install Homebrew

First, you have to install minimum requirements, if the Xcode does not exist on your computer, 
please install it from AppStore or Apple Xcode web site in advance.
Having been installed the Xcode, you can proceed this instruction.  
***If the Xcode and Homebrew is already installed, you shoud skip first section.***
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2. Upgrade Homebrew and update package lists

Second, you have to upgrade homebrew and package repositories.

```bash
brew update && brew upgrade
```

*If you use Fish shell, please run this command.*

```fish
brew update; brew upgrade
```

### 3. Installed minimum requirements

```
brew install node yarn
```


### 4. Install Anaconda using pyenv

Install pyenv with Homebrew running this command.

```
brew install pyenv
```

Check latest Anaconda *3* version. Anaconda2 is only for a Python2, please be careful.

```
pyenv install --list
```

Install latest Anaconda3 by pyenv and this instruction will take for a while.

```
pyenv install anaconda3-5.0.1
```

Succeeding this installation, check the installation running conda command.
If the installation of Anaconda is succeeded, result will show `conda 4.3.30`.

```
conda -V
```

### 5. Create conda environment

Before creating conda environment, upgrade conda itself running below command.

```
conda update conda
```

Next, create conda environemt with Python 3 named `pinna`, and environemnt name is changeable arbitrarily.

```
conda create --name pinna
```

Activate created environment, and then install pipenv.

```
# Activate
conda activate pinna

# Pipenv
pip install pipenv
```

### 6. Configure Pipenv virtualenv & Install Requirements

Create Pipenv virtualenv with Anaconda Python 3.

```
pipenv --python $(conda info --root)/bin/python
```

Install required dependencies using Pipenv, and create virtual Python environment internally.

```
pipenv install
```

### 7. Check Setup Completion

First, you have to enter virtual Python environment defined by pipenv. Entering into pipenv shell is needed for 
development. You have to do this operation to use installed pip packages by Pipenv each time.

```
pipenv shell
```

Almost all setup will be completing soon. To check completion of setting up, launch debugging server for PINNA by `mg s`.
If the server launched properly, all installations have been completed!

```
# move working directory
cd PINNA

# Launch server
mg s
```

### 8. Make secret configuration ***Final Section***

You have to create  `Miragefile.secret` to generate copyrights doc automatically without interactive shell.

```
miragefile: v0.0.1

private_profile:
    name: YOUR_NAME
    email: YOUR_EMAIL_ADDRESS

private_license:
    url: https://github.com/shotastage/pinna-music/blob/master/LICENSE

```
