from setuptools import setup, find_packages

setup(
    name="pofiletranslate",
    version="0.1.0",
    description="A CLI tool for automating PO file translations from local codebase",
    author="Rachid Alassir",
    author_email="rachidalassir@gmail.com",
    packages=find_packages(),
    install_requires=[
        "polib",
    ],
    entry_points={
        "console_scripts": [
            "pofiletranslate=po_translate.cli:main",
        ],
    },
)
