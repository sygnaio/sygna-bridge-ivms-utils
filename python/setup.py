from setuptools import setup, find_packages
import io
import os

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Reads complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


def get_requirements():
    """Reads the requirements file."""
    requirements = read("requirements.txt")
    requirements_list = list(requirements.strip().splitlines())
    if '-i https://pypi.org/simple' in requirements_list:
        requirements_list.remove('-i https://pypi.org/simple')
    return requirements_list


setup(
    name='sygna-bridge-ivms-util',
    version='0.0.7',
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=get_requirements(),
    url='https://github.com/sygnaio/sygna-bridge-ivms-utils',
    license='MIT',
    author='Sygna',
    author_email='sygna.tech@coolbitx.com',
    description='This is a Python library for building IVMS data structure.',
    long_description=read("./README.md"),
    long_description_content_type='text/markdown',
    keywords="sygna-bridge-util sygna bridge sygna-bridge ecosystem ivms",
    python_requires='>=3.7',
)
