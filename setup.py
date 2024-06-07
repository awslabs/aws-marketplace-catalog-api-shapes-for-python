from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setup(
    name="aws-marketplace-catalog-api-shape-library-for-python",
    version="0.1.0",
    author="Amazon Web Services",
    license="Apache License 2.0",
    url="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python",
    description="A Python library containing strongly-typed Entity and Change type shapes for AWS Marketplace Catalog API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    extras_require={
        'test': ['pytest']
    },
)