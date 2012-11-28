import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sites-watchdog",
    version = "1.0.1",
    url = 'http://code.zafu.edu.cn/sites-watchdog',
    license = 'BSD',
    description = "keep watch on services of zafu.",
    long_description = read('README'),

    author = 'fish',
    author_email = 'yuxiaqiao@163.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
