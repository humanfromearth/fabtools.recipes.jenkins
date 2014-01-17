"""
Fabtools recipe to install jenkins

http://jenkins-ci.org/
"""
import os.path

from fabric.api import *
import fabtools
from fabtools.files import is_file
from fabtools import require

JENKINS_CONF = '/etc/default/jenkins'
#JENKINS_CONF = '/etc/sysconfig/jenkins' # redhat


@task
def install_jenkins(local_port=8080,
        server_name='jenkins', port=80):
    """
    Install jenkins
    """

    jenkins_home = '/var/lib/jenkins'

    # Require a recent jenkins
    require.deb.key('9B7D32F2D50582E6', url='http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key')
    require.deb.source('jenkins', 'http://pkg.jenkins-ci.org/debian', 'binary/')
    require.deb.package('jenkins')

    # Configure web server
    require.nginx.server()
    require.nginx.proxied_site(server_name, port=port,
        docroot=jenkins_home,
        proxy_url='http://127.0.0.1:%d' % int(local_port)
        )
