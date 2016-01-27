from setuptools import setup, find_packages

setup(
    name='cvc-password',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        cvc=cvc.cli:run
    ''',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        ],
)

