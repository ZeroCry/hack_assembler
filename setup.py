from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='hack_assembler',
    version='0.3.1',
    description='An implementation of the assembler for the Hack computer.',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Assemblers',
    ],
    keywords='hack assembler nand2tetris',
    url='https://github.com/thiagoalessio/hack_assembler',
    author='Thiago Alessio Pereira',
    author_email='thiagoalessio@me.com',
    license='Apache-2.0',
    packages=['hack_assembler'],
    entry_points={
        'console_scripts': ['hack-assembler=hack_assembler.cli:main'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
)
