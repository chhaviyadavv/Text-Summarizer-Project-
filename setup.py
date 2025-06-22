from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
        # THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS AFTER READING IT FROM THE FILE
        HYPEN_E= "-e ."
        requirements=[]
        with open(file_path) as fileobj:
                requirements=fileobj.readlines()
                requirements=[ req.replace("\n","") for req in requirements]
                if HYPEN_E in requirements:
                        requirements.remove(HYPEN_E)
setup(
        name="Text Summarizer Project",
        version="0.0.1",
        author="Chhavi Yadav",
        author_email="chhavi.yadav91410@gmail.com",
        packages=find_packages(),
        install_requires =get_requirements("requirements.txt")
)