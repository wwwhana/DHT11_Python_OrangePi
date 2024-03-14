from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="OP-dht11",
    version="0.1.0",
    author="lexia",
    author_email="limlexia@gmail.com",
    description="Pure Python library for reading DHT11 sensor on ORANGE PI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wwwhana/DHT11_Python_OrangePi",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
