from setuptools import setup, find_packages

setup(name="selenium_workshop",
    version="0.1.0",
    description="Selenium Workshop",
    author='Baiju Muthukadan',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                      'bottle',
                      'pytest',
                      ],
    )
