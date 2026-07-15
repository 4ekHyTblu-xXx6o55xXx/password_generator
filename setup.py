from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="password-generator",
    version="1.0.0",
    author="Левченко Иван",
    author_email="levchenkoivan3007@gmail.com",
    description="Криптографически безопасный генератор паролей с CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4ekHyTblu-xXx6o55xXx/password_generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pwdgen=password_generator.cli:main",
        ],
    },
)
