=================
cookiecutter-odoo
=================

.. image:: http://img.shields.io/travis/0k/cookiecutter-odoo/master.svg?style=flat
   :target: https://travis-ci.org/0k/cookiecutter-odoo/
   :alt: Travis CI build status

A modified cookiecutter_ template for Odoo.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Maturity
--------

Alpha release. This template uses a modified version of cookiecutter_ templating
system. To install this modified version, please do::

    pip install git+https://github.com/0k/cookiecutter

We plan to have v7 and v8 template in the same repository with sane
branch naming.

We intend to produce compatible and full project for corresponding
`branch in the odoo github repository`_.

.. _branch in the odoo github repository: https://github.com/odoo/odoo/branches


Features
--------

* Include:
  - controllers
  - data
  - i18n
  - models
  - security
  - static (xml, css, js)
  - views
  - wizards


Usage
-----

First install `cookiecutter`_ from 0k's repositories::

    $ pip install git+https://github.com/0k/cookiecutter

Now run with this repo::

    $ cookiecutter gh:elabore-coop/cookiecutter-odoo

Branch selection can be done with ``--checkout``::

    $ cookiecutter gh:0k/cookiecutter-odoo --checkout 16.0

For more info about cookiecutter_ options and usage, please check `cookiecutter documentation`_.

Please bear in mind that we are using a (minor) fork, that should
remain compatible with all cookiecutter's features.

.. _cookiecutter documentation: http://cookiecutter.readthedocs.org/


Contributing
============

Any suggestion or issue is welcome. Push request are very welcome,
please check out the guidelines.


Push Request Guidelines
-----------------------

You can send any code. I'll look at it and will integrate it myself in
the code base and leave you as the author. This process can take time and
it'll take less time if you follow the following guidelines:

- check your python code with PEP8 or pylint. Try to stick to 80 columns wide.
- avoid tabs
- separate your commits per smallest concern.
- each commit should pass the tests (to allow easy bisect)
- each functionality/bugfix commit should contain the code, tests,
  and doc.
- prior minor commit with typographic or code cosmetic changes are
  very welcome. These should be tagged thanks to an ending ``!minor``
  in their commit summary.
- the commit message should follow gitchangelog rules (check the git
  log to get examples)
- if the commit fixes an issue or finished the implementation of a
  feature, please mention it in the summary.

If you have some questions about guidelines which is not answered here,
please check the current ``git log``, you might find previous commit that
would show you how to deal with your issue.


License
=======

Copyright (c) 2012-2015 Valentin Lab.

Licensed under the `BSD License`_.

.. _BSD License: http://raw.github.com/0k/cookiecutter-odoo/master/LICENSE


Thanks
======

- `sudokeys`_ funding this package and providing great `Odoo`_ solutions.

.. _sudokeys: http://www.sudokeys.com
.. _Odoo: http://www.odoo.com
