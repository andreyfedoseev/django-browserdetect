import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-browserdetect',
    version="0.1dev",
    description="A Django app with middleware to detect browser version.",
    long_description=read('README.rst'),
    author='Andrey Fedoseev',
    author_email='andrey.fedoseev@gmail.com',
    license='GPL',
    url='https://github.com/andreyfedoseev/django-browserdetect',
    packages=[
        'browserdetect',
    ],
    install_requires=[
        'zope.cachedescriptors',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
#    test_suite="tests.runtests.runtests",
)
