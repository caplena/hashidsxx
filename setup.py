from distutils.command.build import build

from distutils.core import setup, Extension


# From: https://stackoverflow.com/questions/12491328/python-distutils-not-include-the-swig-generated-module
class CustomBuild(build):
    sub_commands = [
        ('build_ext', build.has_ext_modules),
        ('build_py', build.has_pure_modules),
        ('build_clib', build.has_c_libraries),
        ('build_scripts', build.has_scripts),
    ]


extension_mod = Extension("_hashids_cpp", swig_opts=['-c++'], sources=["hashids_cpp.i", "hashids.cpp"])

setup(
    cmdclass={'build': CustomBuild},
    name="hashids_cpp",
    ext_modules=[extension_mod],
    py_modules=["hashids_cpp"],
    version="0.1",
    license='MIT',
    author='Maurice Gonzenbach',
    author_email='maurice@caplena.com',
    description='Adaptation of hashidsxx to call its c++ funcs from Python',
    long_description='Forked from https://github.com/schoentoon/hashidsxx',
)
