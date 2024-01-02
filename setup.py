from setuptools import setup,find_packages
from typing import List
HYPHEN_E_DOT="-e ."

def read_requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        print("reading requirements")
        requirements=file.readlines()
        if HYPHEN_E_DOT in requirements:
            print("found")
            requirements.remove(HYPHEN_E_DOT)
        requirements=[r.replace("\n","") for r in requirements]
        print(requirements)
        return requirements

setup(
    name="wafer_fault_prediction",
    version="0.0.1",
    author="Linkan Kumar Sahu",
    author_email="sahulinkan7@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt")
)