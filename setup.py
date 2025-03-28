from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    HYPEN_E_DOT='-e .'
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='MLProjects',
    version='0.0.1',
    author='mounika',
    author_email='mounikasurineni2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)