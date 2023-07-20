import setuptools as s
from setuptools import setup, find_packages


with open("README.me","r",encoding = 'utf8') as dd:
  fg = dd.read()

with open("requirement.txt","r") as h:
  require =h.read().split("\n")

s.setup(
  name = "saveMZ",
  version = "1.0",
  author = "Mozan",
  description = "saveMZ is esay save with json file in python",
  packages = s.find_packages("src"),
  package_dir = {"" : "src"},
  url = "https://github.com/imozan/saveMZ.git",
  project_urls={
        "Bug Tracker": "https://github.com/imozan/saveMZ/blob/main/src/save_MZ/__init__.py",
    },
  classifiers = [
    "programming language :: Python :: 3",
    "Operating System :: OS Independent ",
    "License :: OSI Approved :: MIT License "
  ],
  long_description = fg,
  long_description_content_type="text/markdown",
  install_requires = require, 
  python_requires=">=3.6",
)

