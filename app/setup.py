from setuptools import setup, find_packages

setup(
    name='mysite',
    version='1.0',
    long_description=__doc__,
    packages=['mysite'],
    include_package_data=True,
    zip_safe=False,
    install_requires=find_packages(),
    dependency_links=['*']
)