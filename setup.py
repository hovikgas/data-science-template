from setuptools import find_packages, setup


setup(
    name="project_name",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[],
)
