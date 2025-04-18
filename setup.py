import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypackage",
    version="0.0.1",
    author="Jordyn Robare",
    author_email="jrobare@asu.edu",
    description="Python test package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={},
    packages=['mypackage'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=['chemparse', 'numpy', 'rdkit', 'statsmodels', 'pubchempy', 'pandas'],
    package_data={'': ['*.r']},
    include_package_data=True,
    zip_safe=False
)