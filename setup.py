import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findCPcli",
    version="0.0.4",
    author="Alex Oarga",
    author_email="alex718123@gmail.com",
    description="findCP CLI package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/findCP/findCPcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "findCPcore",
    ],
    python_requires='>=3.6',
    scripts=['scripts/findCPcli'],
)
