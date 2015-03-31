from __future__ import unicode_literals
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys



#===================================================================================================
# PyTest
#===================================================================================================
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)



#===================================================================================================
# setup
#===================================================================================================
setup(
    name='xml_factory',
    provides=['xml_factory'],
    version='1.0',

    packages=find_packages(exclude=['tests']),
    install_requires=['six'],
    tests_require=['pytest'],

    cmdclass = {'test': PyTest},


    #===============================================================================================
    # Project description
    #===============================================================================================
    author='Alexandre Motta de Andrade, Diogo de Campos',
    author_email='ama@esss.com.br, campos.ddc@gmail.com',

    url='https://github.com/ESSS/xml_factory',

    license='LGPL v3+',
    description='XMl Factory is a simple XMl writer that uses dict syntax to write files.',
    keywords='xml dict write pretty',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],
)
