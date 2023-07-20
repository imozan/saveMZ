import setuptools as s

with open("README.me","r",encoding = 'utf8') as dd:
  fg = dd.read()

with open("requirement.txt","r") as h:
  require =h.read().split("\n")

s.setup(
  name = "saveMZ",
  version = "1.0",
  author = "Mozan",
  description = "saveMZ is esay save with json file in python",
  packages = s.find_packages(),
  classifiers = [
    "programming language :: Python :: 3",
    "Operating System :: OS Independent ",
    "License :: OSI Approved :: MIT License "
  ],
  long_description = fg,
  install_requires = require 
)

