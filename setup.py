import setuptools

print(setuptools.find_packages(where="src"))

setuptools.setup(
    name = "optimization_utils",
    version = "0.0.5",
    author = "2xic",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
)
