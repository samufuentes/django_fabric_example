import os

from fabric.api import *

env.hosts = ['ubuntu@10.211.55.6']

path, project_name = os.path.split(os.getcwd())
git_repo_remote = 'https://github.com/samufuentes/django_fabric_example.git'

@task
def install_dependancies():
    # To avoid password prompt manually add the following to the
    # /etc/sudoers. Use sudo visudo to edit it
    # ubuntu ALL=(ALL) NOPASSWD: ALL

    sudo("apt-get -y install build-essential")
    sudo("apt-get -y install python-dev")
    sudo("apt-get -y install git-core")
    sudo("apt-get -y install python-setuptools")
    sudo("apt-get -y install nginx")
    sudo("easy_install pip")
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
def configure_server():
    with cd(project_name):
        sudo("cp production_files/uwsgi.conf /etc/init/uwsgi.conf")
        sudo("cp production_files/nginx_example /etc/nginx/sites-available")
        sudo("ln -s /etc/nginx/sites-available/nginx_example /etc/nginx/sites-enabled/nginx_example")

@task
def restart_services():
    run("service nginx restart")
    run("service uwsgi restart")


@task
def first_deploy():
    prepare_dependancies()
    # Avoid rsa prompt
    run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    run("git clone %s" %git_repo_remote)
    create_env()
    install_requirements()
    configure_server()
    restart_services()

@task
def deploy():
    with cd(project_name):
        run("git pull origin master")
    install_requirements()
    restart_services()
