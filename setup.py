from setuptools import setup

setup(
    name='undname',
    version='0.1',
    packages=['undname'],
    url='',
    license='',
    author='Igor Kozyrenko',
    author_email='igor@ikseek.com',
    description='CFFI wrapper for wine undname module',
    setup_requires=["cffi"],
    install_requires=["cffi"],
    cffi_modules=["undname/undname_build.py:ffi_builder"]
)
