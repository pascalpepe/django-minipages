import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-minipages',
    version='0.1.0',
    description='Django application for managing simple web pages.',
    long_description=README,
    long_description_content_type='text/x-rst',
    packages=find_packages(include=['minipages']),
    include_package_data=True,
    author='Pascal Pepe',
    author_email='contact@pascalpepe.fr',
    url='https://www.pascalpepe.com/en/projects/django-minipages/',
    project_urls={
        'Documentation': 'https://pascalpepe.gitlab.io/django-minipages',
        'Source code': 'https://gitlab.com/pascalpepe/django-minipages',
        'Issue tracker': 'https://gitlab.com/pascalpepe/django-minipages/issues',
    },
    license='Apache-2.0',
    keywords='django pages',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
