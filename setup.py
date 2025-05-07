from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prime_analysis_toolkit",
    version="0.1.0",
    author="Michael Lawrenchuk",
    author_email="MichaelLawrenchuk@users.noreply.github.com",
    description="A Python toolkit for generating, analyzing, and visualizing prime numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MikeLawrenchuk/prime_analysis_toolkit",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests", "venv", "*.egg-info"]),
    install_requires=[
        "matplotlib>=3.9,<4",
        "networkx>=2.8",
        "sympy>=1.8",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3",
            "pillow>=11",
        ],
    },
    entry_points={
        "console_scripts": [
            "prime_analysis_toolkit=prime_analysis_toolkit.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
