from setuptools import find_packages, setup

setup(
    name="ml_example",
    packages=find_packages(),
    version="0.1.0",
    description="Ml project for Heart desease prediction",
    author="Andrei Ponomarev",
    install_requires=[
        "click==7.1.2",
        "joblib==1.0.1",
        "marshmallow==3.12.0",
        "marshmallow-dataclass==8.4.1",
        "mypy-extensions==0.4.3",
        "numpy==1.20.3",
        "pandas==1.2.4",
        "python-dateutil==2.8.1",
        "pytz==2021.1",
        "PyYAML==5.4.1",
        "scikit-learn==0.24.2",
        "scipy==1.6.3",
        "six==1.16.0",
        "sklearn==0.0",
        "threadpoolctl==2.1.0",
        "typing-extensions==3.10.0.0",
        "typing-inspect==0.6.0"
    ],
    license="MIT",
)