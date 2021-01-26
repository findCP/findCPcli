import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findCPcli",
    version="0.0.8",
    author="Alex Oarga",
    author_email="alex718123@gmail.com",
    description="findCP CLI package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/findCP/findCPcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "findCPcore",
        "numpy>=1.16.5",
    ],
    python_requires='>=3.5',
    scripts=['scripts/findCPcli'],
)
