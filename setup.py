# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["opencv-python"],    
    entry_points={
        "console_scripts": [
            # format is: "command-name = package_name.file_name:function_name"
            "hide_text = my_package.main:hide_text",
            "show_text = my_package.main:show_text",

        ],
    },
)