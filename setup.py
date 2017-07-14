from setuptools import setup, find_packages

NAME = "pyconfig"
VERSION = "0.1.0"

REQUIRES = [
    "PyYAML"
]

DEPENDENCY_LINKS = [
]

setup(
    name=NAME,
    version=VERSION,
    description="Python configuration loader",
    author_email="dohernandez@gmail.com",
    keywords=["python", "configuration loader"],
    install_requires=REQUIRES,
    packages=find_packages(),
    dependency_links=DEPENDENCY_LINKS
)
