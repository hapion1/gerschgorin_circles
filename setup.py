from setuptools import setup

setup(
    name='gerschgorin_circles',
    version='0.1.0',
    license='MIT',
    author='Jan Piontek',
    author_email='jan-piontek@outlook.de',
    description='Simple Python implementation of Gerschgorin Circles to estimate Eigenvalues. Can also calculate'
                'Eigenvalues and Eigenvectors.',
    requires=[
        'matplotlib',
        'numpy'
    ]
)
