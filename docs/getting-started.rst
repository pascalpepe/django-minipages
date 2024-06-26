===============
Getting started
===============

MiniPages is free and open-source software, distributed under
the `Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.
Being a reusable Django application, you will need to install Python and
Django before you can use it.


Requirements
============

Python and Django compatibility
-------------------------------

This project requires the following:

======= ==========================
Django  Python
======= ==========================
4.2 LTS 3.8, 3.9, 3.10, 3.11, 3.12
------- --------------------------
5.0     3.10, 3.11, 3.12
======= ==========================

We highly recommend the latest release of each series for both Python and
Django.

Python virtual environment
--------------------------

It is highly recommended to install Django, MiniPages, and all other Python
dependencies of your project within
a `Python virtual environment <https://docs.python.org/3/library/venv.html>`_.


Install MiniPages
=================

Get the latest release from PyPI
--------------------------------

This project is released on `PyPI <https://pypi.org/project/django-minipages/>`_,
the Python Package Index. You can install the latest release with pip:

.. code-block:: bash

    pip install django-minipages

Get the latest development version
----------------------------------

.. note::

   This option is not recommended unless you want to try incoming changes. You might
   encounter new bugs in the development version.

You can install the latest development version of this project from
the `Git repository <https://github.com/pascalpepe/django-minipages>`_:

.. code-block:: bash

    pip install git+https://github.com/pascalpepe/django-minipages.git@main#egg=django-minipages


Quick start guide
=================

Settings
--------

Add ``"minipages"`` to your ``INSTALLED_APPS`` setting:

.. code-block:: python

    INSTALLED_APPS = [
        "minipages",
        ...
    ]

URL configuration
-----------------

Include the application URLconf in your project ``urls.py`` like this:

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        ...
        path("pages/", include("minipages.urls")),
    ]

Database
--------

Run ``python manage.py migrate`` to create the database tables.

Create some pages
-----------------

Start the development server and visit http://localhost:8000/admin/ to create
a page. You will need to activate the
`Django admin site <https://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_
for this.

View your pages
---------------

Visit http://localhost:8000/pages/ to view a list of your pages.
