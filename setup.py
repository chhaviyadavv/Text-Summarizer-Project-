import setuptools
from typing import List
 ''' 
def get_requirements(file_path: str) -> List[str]:
    # THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS AFTER READING IT FROM THE FILE
    HYPHEN_E = "-e ."
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements  # ← This return statement was missing!'''
with open("README.md","r",encoding="utf-8") as f:
        long_description=f.read()

setuptools.setup(
    name="Text Summarizer Project",
    version="0.0.0",
    author="Chhavi Yadav",
    author_email="chhavi.yadav91410@gmail.com",
    description="A text summarizer project.",
    long_description=long_description,
    long_description_content="text/markdown"
    url="https://github.com/chhaviyadavv/Text-Summarizer-Project-",
    project_urls={
        "Bug Tracker": "https://github.com/chhaviyadavv/Text-Summarizer-Project-/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)
