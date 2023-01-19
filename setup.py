import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setup(
    name='chatgpt-search',
    version='1.0.0',
    description='A simple example package',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/yourusername/mypackage',
    author='Abhijeet Kumar',
    author_email='iitkgp.abhijeetkumar@gmail.com',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=["search"],
    include_package_data=True,
    install_requires=['dependency1', 'dependency2'],
    entry_points = {
        "console_scripts": [
            "realpython=search.__main__:main",
        ]
    }
)
