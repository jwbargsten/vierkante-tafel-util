import pathlib
from setuptools import setup, find_packages


base_packages = [
    "scipy>=1.8.1",
]

test_packages = [
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "black>=19.3b0",
]

all_packages = base_packages
dev_packages = all_packages + test_packages


setup(
    name="vierkante-tafel-util",
    version="0.0.1",
    author="Joachim Bargsten",
    packages=find_packages('src', exclude=['tests']),
    package_dir={"": "src"},
    description="Help to select people or groups of people in a fair and a bit random way",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/jwbargsten/vierkante-tafel-util/",
    },
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    license_files=("LICENSE",),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
    ],
)
