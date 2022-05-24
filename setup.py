from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in opspiry/__init__.py
from opspiry import __version__ as version

setup(
	name="opspiry",
	version=version,
	description="ERP for Distribution by PT INSPIRY INDONESIA KONSULTAN",
	author="Inspiry",
	author_email="adi.setyono@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
