# Standard Library
import sys
from codecs import open
from os import path

from setuptools import find_packages
from setuptools import setup

assert sys.version_info >= (3, 5, 2), "Websauna needs Python 3.5.2 or newer, you have {version}".format(
    version=sys.version_info)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

with open(path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    CHANGES = f.read()

# trying to run python setup.py install or python setup.py develop
if len(sys.argv) >= 2:
    if sys.argv[0] == "setup.py" and sys.argv[1] in ("install", "develop"):
        # Otherwise so much stuff would be broken later...
        raise RuntimeError(
            "It is not possible to install this package with setup.py. Use pip to install this package as instructed in Websauna tutorial.")

setup(
    name='websauna.newsletter',
    version='1.0a4.dev0',
    description='Newsletter add on for Websauna',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
    url='https://websauna.org',
    author='Mikko Ohtamaa',
    author_email='mikko@opensourcehacker.com',
    license='MIT',
    keywords='web websauna pyramid',
    namespace_packages=['websauna'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='websauna.newsletter',
    python_requires='>=3.5.2',
    install_requires=[
        'websauna[celery]',
        'websauna.magiclogin'
    ],
    extras_require={
        # Dependencies for running test suite
        'test': [
            'codecov',
            'flake8',
            'pytest>=3.0,<4.0',
            'pytest-runner',
            'coverage',
            'flaky',
            'isort',
            'pytest-cov',
            'pytest-runner',
            'pytest-splinter',
            'pytest-timeout',
            'webtest',
        ],
        # Dependencies to make releases
        'dev': [
            'websauna[dev,test]'
        ],
    },

    # Define where this application starts as referred by WSGI web servers
    entry_points={
        'paste.app_factory': [
            'main = websauna.newsletter.demo:main'
        ],
    }
)
