from setuptools import find_packages, setup

setup(
    name='studio',
    version='0.3.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'keras',
        'tensorflow==1.*',
        'pandas',
        'numpy==1.*',
        'talos',
        'sklearn',
        'requests',
        'plotly',
        'tables'
    ],
)
