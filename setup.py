import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='oscar-portation',
    version='0.1.1',
    packages=find_packages(),
    license='BSD License',
    include_package_data=True,
    description='Oscar dashboard app for import/export',
    author='Dima Kovalchuk',
    author_email='dmyutro@ukr.net',
    url='https://github.com/dima-kov/oscar-portation',
    download_url='https://github.com/dima-kov/oscar-portation/archive/v0.1.1.tar.gz',
    keywords=['django', 'oscar', 'export', 'import'],
    install_requires=[
        'openpyxl',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
