#!/bin/env python
from setuptools import setup


setup(
    name='zerotk.xml_factory',
    use_scm_version=True,

    author='Alexandre Andrade, Diogo de Campos',
    author_email='kaniabi@gmail.com, campos.ddc@gmail.com',

    url='https://github.com/zerotk/reraiseit',

    description='XML/Dict/Json Generator.',
    long_description='''XMl Factory is a simple XMl writer that uses dict syntax to write files.''',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    include_package_data=True,

    packages=['zerotk', 'zerotk.xml_factory'],
    namespace_packages=['zerotk'],

    keywords=['xml', 'dict', 'json', 'generator', 'pretty'],

    install_requires=['six'],
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest', 'coverage', 'cogapp', 'pytest-datadir'],
)
