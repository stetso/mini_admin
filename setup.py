from setuptools import setup, find_packages

setup(
    name='mini_admin',
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mini_admin=backend.app:cli',
        ],
    },
    install_requires =[
        "Flask==1.1.1",
        "Flask-Cors==3.0.9",
        "pony==0.7.10"
    ]
)