TestRest
========

POC Testing framework for RESTfull services testing. It allows you to define all your tests in a YAML file - without writing any code.

Installation
============
* Clone this repo.
* You'll need a RESTfull services you would like to test.

Prereq
======

You need to have python3 and the yaml module installed.

Usage
=====

```bash
python3 src/TestRest.py -c config/testRestConfig.yaml

```

Config
======

The config file you find in the repo tests the dropwizard project introduced by the fine book 

RESTful Web Services with Dropwizard<br />
Alexandros Dallas<br />
Release Date: February 2014<br />
ISBN: 1783289538<br />
ISBN 13: 9781783289530

It's worth buying - http://www.packtpub.com/restful-web-services-with-dropwizard/book
