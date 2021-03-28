import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()

setuptools.setup(name = 'text_preprocessing',
	             version = '0.0.1',
	             auther = 'Sejal', 
	             auther_email = 'sejalpatel133@gmail.com',
	             description = 'This is text preprocessing package',
	             Long_description = long_description, 
	             long_description_content_type = 'text/markdown',
	             package = setuptools.find_packages(),
	             classifiers = ['Programming Language :: Python :: 3', 
	                             'Operating system :: OS Independent']
	             python_requires = '>=3.5')
