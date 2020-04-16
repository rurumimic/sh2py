import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='sh2py-rurumimic',
  version='0.0.1',
  author='rurumimic',
  author_email='unhyop@gmail.com',
  description='Shell script to Python code.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/rurumimic/sh2py',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)
