from setuptools import setup, find_packages

setup(
    name="helm-doc",
    version="0.1.0",
    py_modules=[
        "helmdoc",
    ],
    package=find_packages(),
    install_requires=["wheel", "Click", "pyyaml"],
    entry_points="""
        [console_scripts]
        helm-doc=helmdoc:cli
    """,
)
