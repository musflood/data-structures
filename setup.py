from setuptools import setupt 

setup(
    name = 'data-structures',
    description = 'A number of classic data structures impemented in python',
    package_dir = {'': 'src'},
    py_modules = [],
    authors = 'Megan, Kavdi',
    author_email = 'kavdyjh@gmail.com',
    install_requires = [],
    extras_require = {
        'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
    }
)