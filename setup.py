from setuptools import find_packages, setup
from typing import List

## -e . in requirements.txt will automatically trigger setup.py
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[list]:
    """
    Returns a list of requirements from requirements.txt file

    Args
      file_path - path for requirements.txt

    Returns
      List[list] Returns a list of libraries
    
    get_requirements(file_path=)
    """
    #pass
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='0760_20_01_ML_Students_Performance',
    version='0.0.1',
    author='Luismbpr',
    author_email='97373331+Luismbpr@users.noreply.github.com',
    packages=find_packages(),
    #install_requires=['numpy', 'pandas', 'seaborn']
    install_requires=get_requirements(file_path='requirements.txt')
)