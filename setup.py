from setuptools import setup


setup(name='Henyo',
      description='Pinoy Henyo on the web',
      version='1.0',
      author='Jesse Panganiban',
      author_email='me@jpanganiban.com',
      py_modules=['henyo'],
      entry_points={
          'console_scripts': ['henyo = henyo:start']
        },
      install_requires=[
          'flask',
        ],
      )
