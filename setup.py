from setuptools import setup, find_packages

__pckg__ = "date"
__dpckg__ = __pckg__.replace("-", "_")
__version__ = "0.0.1"

setup(
    name=__pckg__,
    version=__version__,
    description="Some description",
    author="Dima",
    author_email="some@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={
        "tests": [
            "pytest==6.2.2",
            "pytest-cov==2.11.1",
        ],
    },
)
