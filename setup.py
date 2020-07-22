import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ViPsy", # Replace with your own username
    version="0.0.1",
    author="INVOLAB",
    author_email="involabad@gmail.com",
    description="ViPsy v0.0.1 is a package which includes Virtual Psychologist bot tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
