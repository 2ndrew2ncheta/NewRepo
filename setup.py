import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='NewRepo', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.5',
    author='Andrew', ## your name
    author_email='sjnews@gmail.com', ## your email
    description='Demo on pip package creation', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/2ndrew2ncheta/NewRepo/',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/2ndrew2ncheta/NewRepo/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['mathFunctions'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)
