from setuptools import setup

setup(
    name='rdsctl',
    version='1.0',
    py_modules=['rdsctl'],
    install_requires=[
        'click',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'rdsctl = rdsctl:cli',
        ],
    },
)
