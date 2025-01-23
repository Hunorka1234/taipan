from setuptools import setup, find_packages

setup(
    name="taipan-language",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'kivy>=2.2.1',
    ],
    entry_points={
        'console_scripts': [
            'taipan=taipan_framework.taipan:main',
        ],
    },
    author="Nagy Hunor Máté",
    author_email="hunoramester@gmail.com",
    description="Taipan Programming Language",
    url="https://github.com/yourusername/taipan",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: UNIX based",
    ],
)
