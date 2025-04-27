from setuptools import setup, find_packages

setup(name="pywhiten2",
      version="2.0.0",
      description="A python package for conducting Lomb-Scargle-based prewhitening of stellar time series.",
      url="https://www.github.com/erikstacey/pywhiten",
      author="Erik William Stacey",
      author_email = "erik@erikstacey.com",
      license="MIT",
      packages= find_packages(where='.'),
      install_requires=[
            "numpy",
            "matplotlib",
            "scipy",
            "astropy"
      ],
      tests_require=["pytest"],
      zip_safe = False,
      include_package_data=True,
      package_data={'': ['cfg/default.toml']},
      )