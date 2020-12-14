from setuptools import setup

setup(
    name='helm-doc',
    version='0.1',
    py_modules=['helmdoc',],
    install_requires=[
        'Click',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        helm-doc=helmdoc:cli
    ''',
)