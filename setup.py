from setuptools import setup, find_packages

setup(
    name='prime_analysis_toolkit',
    version='0.1.0',
    description='A toolkit for analyzing prime numbers',
    author='Your Name',
    packages=find_packages(),
    install_requires=['numpy'],  # Add other dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
