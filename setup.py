from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of libraries in requirements.txt file.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ML_project",
    version="0.1",
    author="Ashish Raj",
    author_email="ashish.raj.dev04@gmail.com",
    description="A end to end ML project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
