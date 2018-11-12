<p align="center">
<a href="https://github.com/crd/the-queens-mirror/blob/master/LICENSE"><img alt="BSD 3-Clause License" src="https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square"></a>
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# the-queens-mirror
Alexa Skill and backing Lambda for The Queen's Mirror, a Skill used by my family to reveal a dining reservation to our children.

# What's in the Box

This repository contains the intent necessary to set up the Alexa Skill as well as everything you need to deploy the Lambda.

# Prerequisites

I'd recommend having `pipenv` and `pyenv` installed and knowing how they work.

# How to Build the Lambda

It's necessary to first collect and package all the dependencies:

```
$ git clone git@github.com:crd/the-queens-mirror.git
$ cd the-queens-mirror/lambda/py
$ pipenv sync
$ cd $(eval pipenv --venv)/lib/python3.6/site-packages/
$ zip -r9 the-queens-mirror.zip .
```

Next add the lambda itself to the .zip file:

```
$ zip -g the-queens-mirror.zip lambda_function.py
```

You're now ready to upload the .zip file to the Lambda console.
