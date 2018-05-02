from setuptools import setup

setup(
    name='undname',
    version='0.1',
    packages=['undname'],
    url='https://github.com/ikseek/undname',
    license='LGPLv2.1',
    author='Igor Kozyrenko',
    author_email='igor@ikseek.com',
    description='CFFI wrapper for wine undname module',
    long_description=open('README.rst').read(),
    keywords=['undname', 'msvc'],
    setup_requires=["cffi"],
    install_requires=["cffi"],
    cffi_modules=["undname/undname_build.py:ffi_builder"],
    classifiers=["Development Status :: 4 - Beta",
                 "Topic :: Software Development :: Debuggers",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved"
                 " :: GNU Lesser General Public License v2 or later (LGPLv2+)"]
)
