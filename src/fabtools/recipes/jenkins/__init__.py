"""
Fabtools recipe to install jenkins

http://jenkins-ci.org/
"""
import os.path

from fabric.api import *
import fabtools
from fabtools.files import is_file
from fabtools import require

JENKINS_CONF = '/etc/sysconfig/jenkins'
#JENKINS_CONF = '/etc/sysconfig/jenkins'

@task
def install_jenkins(jenkins_home, local_port=6000,
        server_name='jenkins', port=80):
    """
    Install jenkins
    """

    require.directory(jenkins_home, owner=env.user, use_sudo=True)

    # Require a recent jenkins
    require.deb.key('jenkins-ci.org.key', url='http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key')
    require.deb.source('jenkins', 'http://pkg.jenkins-ci.org/debian', 'binary/')
    sudo("apt-get -qq update")
    require.deb.package('jenkins')

    return
    # Carbon config file
    with cd('conf'):
        if not is_file('carbon.conf'):
            run('cp carbon.conf.example carbon.conf')
        require.file('storage-schemas.conf', contents=STORAGE_SCHEMA)

    # Configure web server
    require.nginx.server()
    require.nginx.proxied_site(server_name, port=port,
        docroot=jenkins_home,
        proxy_url='http://127.0.0.1:%d' % int(local_port)
        )
