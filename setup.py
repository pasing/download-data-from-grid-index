from setuptools import setup, find_packages

requirements = [
    'geopandas==0.14.1',
    'argparse==1.4.0',
    'requests==2.31.0'
]

setup(
    name='download-data-from-grid-index',
    version='0.1',
    author="Pasquale Inglese",
    author_email='pasqualeinglese@gmail.com',
    url='https://github.com/pasing/download-data-from-grid-index',
    license='MIT',
    description='Download data from grid index',
    python_requires='>=3.6',
    install_requires=requirements,
    packages=find_packages(include=['download_data_from_grid_index'])
)
