from distutils.core import setup

setup(
    name='samplepackage',
    version='0.1.0',
    author='John Doe',
    author_email='ex@example.com',
    packages=["easylog"],
    scripts=[],
    url='http://www.example.com',
    license='LICENSE.txt',
    description='A sample Python package of modules.',
    long_description=open('README.rst').read(),
    install_requires=[],
)