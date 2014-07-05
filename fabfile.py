from fabric.api import *

env.hosts = ['ubuntu@10.211.55.6']

@task
def deploy_staging():
    run('touch test.tst')
