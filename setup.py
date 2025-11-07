from setuptools import find_packages,setup
from typing import List

H_E_D='-e .'
def get_requirents(file_path:str)->List[str]:
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[req.replace("\n","") for req in req]
        if H_E_D in req:
            req.remove(H_E_D)
    return req        



setup(
    name="Mlproject",
    version="0.0.1",
    author="Manu Amidal",
    author_email="manuamidal@gmail.com",
    packages=find_packages(),
    install_requires=get_requirents("requirements.txt")
)

