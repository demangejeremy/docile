import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='docile',  
     version='0.0.2',
     scripts=['docile'] ,
     author="Jérémy DEMANGE",
     author_email="j@lachainemedias.com",
     description="Your automated Python documentation.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/demangejeremy/docile",
     packages=setuptools.find_packages(),
     install_requires=[
        'click'
    ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )