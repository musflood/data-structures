from setuptools import setup

setup(
    name='data-structures',
    description='A number of classic data structures impemented in python',
    package_dir={'': 'src'},
    py_modules=['linked_list', 'stack', 'dll', 'que_', 'deque', 'binheap'],
    authors='Megan, Kavdi',
    author_email='kavdyjh@gmail.com',
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
    }
)
