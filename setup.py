from setuptools import setup, find_packages

setup(
    name='pymogile',
    version='2.0.3',
    description="pymogile",
    long_description="""Python MogileFS Client""",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    author='AloneRoad',
    author_email='aloneroad@gmail.com',
    maintainer='Devin Barry',
    maintainer_email='devinbarry@gmail.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=['six>=1.9.0'],
    test_suite='tests',
    tests_require=['tox'],
    include_package_data=True,
    zip_safe=False
)
