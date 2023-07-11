from setuptools import setup, find_packages
from typing import List



def parse_requirements(file_path:str)->List[str]:
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n"," ") for req in requirements ]
        

    
    return requirements 


setup(
    name='MLProject',
    version='1.0.0',
    author='Chijioke',
    author_email='c.iwuchukwu@yahoo.com',
    description='Description of your package',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt')

)