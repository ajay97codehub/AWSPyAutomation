# setup.py

from setuptools import setup, find_packages

setup(
    name='awspyautomation',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3',
        'click',
        # Add any additional dependencies here
    ],
    entry_points={
        'console_scripts': [
            'awspyautomation=awspyautomation.cli:cli',
        ],
    },
)
