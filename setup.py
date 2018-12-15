import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as readme:
    README = readme.read()

setup(
    name="colorizer",
    version="1.0.0",
    description="Easily print colored text",
    long_description=README,
    url="https://github.com/mlevesquedion/colorizer",
    author="Michaël Lévesque-Dion",
    author_email="mlevesquedion@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["colorizer"],
    include_package_data=True,
    install_requires=[
        "colorama"
    ],
)
