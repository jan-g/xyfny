import os.path
from setuptools import setup, find_packages


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()
setup(
    name="xyfny",
    version="0.0.1",
    description="Reworking of xyppy",
    long_description=read_file("README.md"),
    author="jang",
    author_email="faastm@ioctl.org",
    license=read_file("LICENSE"),
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
)


