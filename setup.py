import setuptools

from os import path


PWD = path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(PWD, "README.rst")) as f:
        return f.read()


setuptools.setup(
    name="celestine",
    version="0.1.1",
    author="Lucas Maystre",
    author_email="lucas@maystre.ch",
    description="Knowledge management system.",
    long_description=readme(),
    url="https://github.com/lucasmaystre/celestine",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="zettelkasten knowledge information notes",
    packages=setuptools.find_packages(),
    install_requires=[
        "sh",
        "Click",
    ],
    tests_require=[
        "pytest",
    ],
    entry_points="""
        [console_scripts]
        ct=celestine.main:main
    """,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
)
