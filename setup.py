from setuptools import setup, find_packages

setup(
    name='prime_analysis_toolkit',
    version='0.1.0',  # Update as needed
    description='A Python toolkit for generating, analyzing, and visualizing prime numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',  # Replace with your name
    author_email='your_email@example.com',  # Replace with your email
    url='https://github.com/your-username/prime_analysis_toolkit',  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pytest',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
