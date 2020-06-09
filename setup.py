from setuptools import setup

setup(
    name="sync_location",
    version="1.0.0",
    author="Jelmer van Arnhem",
    description="Read, parse and expose syncthing folder locations by name",
    license="MIT",
    py_modules=["sync_location"],
    include_package_data=True,
    python_requires=">= 3.*",
    setup_requires=["setuptools"],
    entry_points={"console_scripts": ["sync_location= sync_location:main"]}
)
