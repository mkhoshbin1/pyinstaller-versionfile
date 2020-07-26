import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION.txt", "r") as fh:
    version = fh.read().strip()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('./src/pyinstaller_versionfile')


setuptools.setup(
    name="pyinstaller_versionfile",
    version=version,
    author="Andreas Finkler",
    author_email="andi.finkler@gmail.com",
    description="Create a version file from a simple YAML config file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="svn://nas/refarch/pyinstaller-versionfile",
    packages=setuptools.find_packages(where="src"),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
          'console_scripts': [
              'create-version-file = pyinstaller_versionfile.create_version_file:main'
          ]
      },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*'
)