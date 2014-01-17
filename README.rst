Description
===========

`Fabric <http://fabfile.org/>`_ task to install `jenkins <http://jenkins-ci.org/>`_, using `fabtools <http://github.com/ronnix/fabtools>`_.

How to use
==========

Import the task in your project's ``fabfile.py`` to make it available::

    from fabtools.recipes.jenkins import install_jenkins

Then you can call it from the ``fab`` command::

    fab install_jenkins
