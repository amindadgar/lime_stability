from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lime_stability',
    version='0.1.2',
    author="Giorgio Visani",
    author_email="giorgio.visani2@unibo.it",
    description="A package to evaluate Lime stability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giorgiovisani/lime_stability.git",
    packages=['lime_stability'],
    install_requires=[
        'lime',
        'statsmodels',
        'statistics',
        'numpy==1.26.4',
        'scikit-learn==1.1.3'
    ],
    license='BSD',
    zip_safe=False)
