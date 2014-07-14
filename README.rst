.. image:: https://travis-ci.org/samufuentes/django_fabric_example.svg?branch=master
    :target: https://travis-ci.org/samufuentes/django_fabric_example


Django Fabric Example
=====================

Django Fabric Example is a simple fabric script to deploy a Django system remotely. The server stack is the following

* Django 1.6
* uwsgi
* nginx
* celery

The script is tested with an Ubuntu 14.04 LTS created in Amazon from an AMI. Previous to running the script you need to obtain the .pem credentials. In addition to avoid password prompt manually add the following to the /etc/sudoers. Use sudo visudo to edit it::

    ubuntu ALL=(ALL) NOPASSWD: ALL

You can trigger the first deployment on a new server entering the directory of the project and running::

    $ fab first_deploy -i /path/to/your.pem -H user@server

Subsequent deploys go like this::

    $ fab deploy -i /path/to/your.pem -H user@server

Important information
~~~~~~~~~~~~~~~~~~~~~

There are examples of the configuration of the services in the folder "production_files". They use default values that you might want to adapt to your needs.

The script is not doing anything with the statics or with the DB. You need to add those to the configuration.

Auto-deploy
~~~~~~~~~~~

There's also an example on how to build an auto deploy system with a URL and a github hook. If you don't want it, comment out the corresponding url in urls.py

By default the server will redeploy when the URL /autodeploy/ gets hit. You can configure a github hook to go there after successful merge, for instance. Right now it doesn't authenticate github, i.e. anybody hitting that URL will force a redeploy.
