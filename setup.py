from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> list[str]:
    '''
    This function return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('/n', '') for req in requirements if not req == "-e ."]
    return requirements

setup(

    name = 'mlproject',
    version= '0.0.1',
    author = 'Dinesh Vennapoosa',
    author_email= 'diniprasad49149@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)