from setuptools import setup, find_packages
import sys

install_requires = ['django>=1.3']


setup(
    name = "django-initkit",
    version = '0.0.1',
    url = 'http://fitoria.net/',
    author = 'Adolfo Fitoria',
    author_email = 'adolfo.fitoria@gmail.com',
    description = 'A personalized django startproject command',
    packages = find_packages(),
    scripts = ['initkit/django_initkit.py'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
