import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


from setuptools import find_packages

setuptools.setup(
    name="gwparents", # Replace with your own username
    version="0.5.0",
    author="Simone Mastrogiovanni",
    author_email="mastrogiovanni.simo@gmail.com",
    description="A package to use syntehtic population of binaries to fit GW events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="gihub hutl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pycbc', 'lalsuite', 'seaborn','bilby','daft'],
    python_requires='>=3.9',
)
