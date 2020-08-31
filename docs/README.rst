=======================
miniPages documentation
=======================

The documentation of miniPages is written
in `reStructuredText <https://docutils.sourceforge.io/rst.html>`_ and built
with `Sphinx <https://www.sphinx-doc.org/en/master/>`_. You can read it:

- at https://pascalpepe.gitlab.io/django-minipages,
- in plain text in this directory,
- or by building a local version on your computer.


Building a local version
========================

The easiest way to build a local version of the documentation is by using
the `tox <https://tox.readthedocs.io/en/latest/>`_ command line that is
already included in the project:

1. Get the project source code from its `Git repository <https://gitlab.com/pascalpepe/django-minipages.git>`_:

   .. code-block:: bash

       git clone https://gitlab.com/pascalpepe/django-minipages.git

2. Install tox (preferably within a `Python virtual environment <https://docs.python.org/3/library/venv.html>`_):

   .. code-block:: bash

       pip install tox

3. Run the following command to install all dependencies and compile the
   documentation:

   .. code-block:: bash

       tox -e docs-public

4. The HTML pages can be found in the ``public/`` directory. Open
   ``index.html`` in your favorite web browser to start reading the
   documentation.


License
=======

The documentation of this project is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-sa/4.0/>`_.

Code samples and snippets found in the documentation are licensed under the
`Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_, same as
the project source code.
