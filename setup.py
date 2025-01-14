from setuptools import setup, find_packages

setup(
    name='rocketdoo',
    version='1.0',
    description='This library allows you to build an automated local development environment for Odoo EE and CE.'
    long_description=open('README.md',encoding='utf-8').read(),
    author='Horacio Montaño and Elias Braceras',
    author_email='horaciomontano@hdmsoft.com.ar',
    url='https://github.com/HDM-soft/rocketdoo.git',
    packages=find_packages(),
    install_requires=[
        'copier',  # Asegúrate de incluir copier en las dependencias
        # Incluye aquí cualquier otra dependencia que tu proyecto necesite
    ],
    entry_points={
        'console_scripts': [
            'rocketdoo=rocketdoo:main',
        ],
    },
)
