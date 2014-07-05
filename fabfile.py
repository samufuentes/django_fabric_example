import os

from fabric.api import *

env.hosts = ['ubuntu@10.211.55.6']

path, project_name = os.path.split(os.getcwd())
git_repo_remote = 'https://github.com/samufuentes/django_fabric_example.git'

@task
def prepare_dependancies():
    # To avoid password prompt manually add the following to the
    # /etc/sudoers. Use sudo visudo to edit it
    # ubuntu ALL=(ALL) NOPASSWD: ALL
    sudo("apt-get -y install git-core", shell=False) # shell=False avoids pwd prompt. -y avoids confirmation prompt

@task
def first_deploy():
    prepare_dependancies()
    # Avoid rsa prompt
    run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    run("git clone %s" %git_repo_remote)

@task
def deploy_staging():
    pass
