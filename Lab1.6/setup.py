from Cython.Build.Dependencies import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        "sort_cython.pyx", compiler_directives={"language_level": "3"}
    )
)
