from fabric.api import *

env.user = 'no'
env.hosts = ['nerdha.us']

def debug():
    from nerdhaus import app
    app.run(host="192.168.0.165", port=9002)

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/%s.tar.gz' % dist)
    with cd('/tmp'):
        run('tar xzf /tmp/%s.tar.gz' % dist)
        with cd('%s' % dist):
            run('/var/www/nerdha.us/env/bin/python setup.py install')

    run('rm -rf /tmp/%s /tmp/%s.tar.gz' % (dist, dist))
