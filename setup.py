
from setuptools import setup, find_packages
import sys, os

setup(name='netopsdeploy',
    version='1.0',
    description="Admin functions for Netops Device Deployment",
    long_description="Admin functions for Netops Device Deployment",
    classifiers=[],
    keywords='',
    author='Nathan Gotz',
    author_email='nathan@gotz.co',
    url='https://github.com/nlgotz/netopsdeploy',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        netopsdeploy = netopsdeploy.cli.main:main
    """,
    namespace_packages=[],
    )
