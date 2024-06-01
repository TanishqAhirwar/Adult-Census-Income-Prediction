from setuptools import find_packages,setup 

def get_requirements()->list[str]:

    requirements_list : list[str] = []

    return requirements_list


setup(
    name = "Adult Census Income Prediction",
    version = "0.0.1",
    author="TanishqAhirwar",
    author_email="tanishqahirwar258@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)