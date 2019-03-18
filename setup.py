import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PVOutputAPI",
    version="0.0.1",
    author="Josenivaldo Benito Junior",
    author_email="jrbenito@benito.qsl.br",
    description="Wraps API calls to pvoutput.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrbenito/pvoutput",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
