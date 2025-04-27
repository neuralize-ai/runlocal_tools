from setuptools import setup, find_packages

# This file provides a fallback for older build systems
# Most configuration is in pyproject.toml

setup(
    name="runlocal_tools",
    version="0.0.1",
    description="Tools to run models from different frameworks via a common interface",
    author="RunLocal",
    author_email="founders@runlocal.ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
) 