from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Getting version
with open(path.join(here, '{{cookiecutter.app_name}}', 'version.py'), encoding='utf-8') as f:
    exec(f.read())

# Get the long description from the file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs]

setup(
    name='{{cookiecutter.app_name}}',
    version=__version__,
    description='{{cookiecutter.project_short_description}}',
    long_description=long_description,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/tarball/' + __version__,
    license='{{cookiecutter.open_source_license}}',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='{{cookiecutter.full_name}}',
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author_email='{{cookiecutter.email}}'
)
