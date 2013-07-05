from fabric.api import *

env.user = 'no'
env.hosts = ['nerdha.us']

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/nerdhaus.tar.gz')
    run('mkdir /tmp/nerdhaus')
    with cd('/tmp/nerdhaus'):
        run('tar xzf /tmp/nerdhaus.tar.gz')
        run('/var/www/nerdhaus/web/env/bin/python setup.py install')
    run('rm -rf /tmp/nerdhaus /tmp/nerdhaus.tar.gz')
