from setuptools import setup, find_packages

setup(
    name="po-translate",
    version="0.1.0",
    description="A CLI tool for automating PO file translations",
    author="Rachid Alassir",
    author_email="rachidalassir@gmail.com",
    packages=find_packages(),
    install_requires=[
        "polib",
    ],
    entry_points={
        "console_scripts": [
            "po-translate=src.po_translate.cli:main",
        ],
    },
)
