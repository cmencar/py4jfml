import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py4jfml',
    version="0.1",
      author='Corrado Mencar',
      author_email='corrado.mencar@uniba.it',
      description='A Python wrapper for JFML',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://www.uco.es/JFML/',
    packages=setuptools.find_packages(),
    #include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.xml' ],
        # And include any *.msg files found in the 'hello' package, too:
        'jar_files': ['*.jar']
    },
    install_requires="py4j",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",  
        "Programming Language :: Python :: 3.5",  
        "Topic :: Software Development :: Version Control :: Git",
    ],
)

#from setuptools import setup, find_packages

#setup(
#    name='py4jfml',
#      version='0.1',
#      description='A Python wrapper for JFML',
#      url='http://www.uco.es/JFML/',
#      author='Corrado Mencar',
#      author_email='corrado.mencar@uniba.it',
#      license='Open Source - GPLv3',
#      packages=find_packages(),
#      install_requires=[ 'py4j'],
#      include_package_data=True,
#      zip_safe=False)

