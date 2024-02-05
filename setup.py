from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

extensions = [
    Extension("greeter.server", ["greeter/server.py"]),
    Extension("greeter.client", ["greeter/client.py"]),
]

setup(
    name="grpc_hello_world",
    version="0.1",
    packages=find_packages(),
    ext_modules=cythonize(extensions),
)
