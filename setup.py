from setuptools import setup

long_description = """
# Python Twine CI Testing
""".strip()

setup(
    name="python-twine-ci-testing",
    version="9641",
    description="Testing some things to fix a build error",
    author="jmerle",
    url="https://github.com/jmerle/python-twine-ci-testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "clr"
    ],
    package_data={
        "clr": ["*.py", "*.pyi"]
    }
)
