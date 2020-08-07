from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    readme = f.read()

setup(
    name="ewo.py",
    author="LyricLy",
    url="https://github.com/LyricLy/ewo.py",
    version="0.1.0",
    license="Blue Oak Model License 1.0.0",
    description="A package to interface with the Emu War Online API.",
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements
)
