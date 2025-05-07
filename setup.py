
from setuptools import setup, find_packages

setup(
    name='prime_analysis_toolkit',
    version='0.1.0',
    description='A Python toolkit for generating, analyzing, and visualizing prime numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mike Lawrenchuk',
    author_email='MikeLawrenchuk@users.noreply.github.com',
    url='https://github.com/MikeLawrenchuk/prime_analysis_toolkit',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pytest',
        'sympy',
        'networkx',
    ],
    entry_points={
        'console_scripts': [
            # CLI for prime-vowel visualizations
            'prime-vowel=prime_analysis_toolkit.prime_vowel:main',
            # CLI for core toolkit (generate/primes/twin-primes/density)
            'prime-toolkit=prime_analysis_toolkit.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
