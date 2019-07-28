import os.path
from setuptools import setup, find_packages


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()


setup(
    name="xyfny",
    version="0.0.10",
    description="Reworking of xyppy",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="theinternetftw, jang",
    author_email="xyfny@ioctl.org",
    license="MIT License",
    url="https://github.com/jan-grant/xyfny",
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'slackbot = slacker.app:main',
        ],
    },

    include_package_data=True,

    install_requires=[],

    tests_require=[
        "pytest",
        "flake8",
        "wheel",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
)
