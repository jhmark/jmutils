import os
from setuptools import setup

setup(
    name = "jmutils",
    version = "1.0.0",
    author = "Jonathan Mark",
    author_email = "jhmark@xenops.com",
    description = ("Utility code in Python 3"),
    license = "MIT",
    keywords = "utilities",
    url = "",  # TODO
    packages=['jmutils'],
    include_package_data=True,
    long_description=open(
      os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
