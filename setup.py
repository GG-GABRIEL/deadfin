from distutils.core import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="deadfin",  # How you named your package folder (MyLib)
    version="0.1.0",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A custom fork of the Redfin library with enhanced cookie management.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gabriel Jordao",  # Type in your name
    packages=setuptools.find_packages(),
    author_email="gabriel.jordao.data@gmail.com",  # Type in your E-Mail
    url="https://github.com/GG-GABRIEL/deadfin",  # Provide either the link to your github or to your website
    keywords=["redfin", "api", "wrapper"],  # Keywords that define your package best
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
