from setuptools import setup

setup(
    name='chunker',
    version='0.1.0',
    author='Ronan Murphy',
    author_email='ronan.murphy@globality.com',
    packages=['chunker'],
    scripts=['scripts/chunker'],
    url='https://www.globality.com/',
    license='LICENSE.txt',
    description='Chunk things!',
    long_description=open('README.md').read(),
    install_requires=[
      "typer",
    ],
)
