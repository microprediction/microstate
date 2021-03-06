import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="microstate",
    version="0.2.0",
    description="Experimental standalone state storage service for crawlers at www.microprediction.org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/microstate",
    author="microprediction",
    author_email="info@microprediction.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["microstate"],
    test_suite='pytest',
    tests_require=['pytest', 'microconventions', 'fakeredis','deepdiff'],
    include_package_data=True,
    install_requires=["microconventions>=0.1.0", "redis","fakeredis", "numpy", "pathlib","requests","getjson"],
    entry_points={
        "console_scripts": [
            "microstate=microstate.__main__:main",
        ]
    },
)
