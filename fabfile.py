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

    # shell=False avoids pwd prompt. -y avoids confirmation prompt
    sudo("apt-get -y install git-core python-setuptools", shell=False)
    sudo("easy_install pip", shell=False)
    sudo("pip install virtualenv")

@task
def create_env():
    with cd(project_name):
        run("virtualenv env")

@task
def install_requirements():
    with cd(project_name):
        run("env/bin/pip install -r requirements.txt")

@task
def first_deploy():
    prepare_dependancies()
    # Avoid rsa prompt
    run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    run("git clone %s" %git_repo_remote)
    create_env()
    install_requirements()

@task
def deploy():
    with cd(project_name):
        run("git pull origin master")
    install_requirements()
