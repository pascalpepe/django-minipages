=======================
miniPages documentation
=======================

The documentation of miniPages is written
in `reStructuredText <https://docutils.sourceforge.io/rst.html>`_ and built
with `Sphinx <https://www.sphinx-doc.org/en/master/>`_. You can read it:

- at https://github.com/pascalpepe/django-minipages/tree/main/docs,
- in plain text in this directory,
- or by building a local version on your computer.


Building a local version
========================

1. Get the project source code:

   .. code-block:: bash

       git clone https://github.com/pascalpepe/django-minipages
       cd django-minipages/

2. Install dependencies (preferably within a `Python virtual environment <https://docs.python.org/3/library/venv.html>`_):

   .. code-block:: bash

       python -m pip install -e .
       python -m pip install -r docs/requirements.txt

3. Build the documentation:

   .. code-block:: bash

       cd docs/
       make html

4. The HTML pages can be found in the ``_build/`` directory. Open
   ``index.html`` in your favorite web browser to start reading the
   documentation.


License
=======

The documentation of this project is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-sa/4.0/>`_.

Code samples and snippets found in the documentation are licensed under the
`Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_, same as
the project source code.
