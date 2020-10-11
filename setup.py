from setuptools import setup

setup(
    name='bdtk',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    scripts=['BDTK'],                  # The name of your scipt, and also the command you'll be using for calling it
    url='https://github.com/aurumkathuria/BDToolkit',
    author='Aurum Kathuria',
    author_email='armkatspamblocker@gmail.com',
    license='MIT',
    install_requires=['pandas>=0.25.1',
                      'numpy>=1.16.5', 
                      'seaborn>=0.9.0',
                      'matplotlib>=3.1.1',
                      'ipywidgets>=7.5.1'
                     ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Data Science\Analytics',
        'License :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    
)