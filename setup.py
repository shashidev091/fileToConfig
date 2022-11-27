from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Convert any file into config file and return an dictionary'
LONG_DESCRIPTION = 'A package that allows to Convert any file into config file and return an dictionary.'

# Setting up
setup(
    name="fileToConfig",
    version=VERSION,
    author="shashi_as_redpanda (Shashi Bhagat)",
    author_email="<skujur871@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[''],
    keywords=['python', 'dotenv', '.env', 'convert file to env', 'env', 'env to dict', 'env to json', 'envToJson'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)