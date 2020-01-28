"""Setup for the deepracer-vehicle-api package."""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Chi Thu Le",
    author_email="thu2004@yahoo.se",
    name='deepracer-vehicle-api',
    license="MIT",
    description='deepracer-vehicle-api is a python package for control the DeepRacer vehicle via HTTP API.',
    version='0.0.5',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/thu2004/deepracer-vehicle-api',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
    install_requires=["beautifulsoup4>=4.8.2","bs4>=0.0.1","lxml>=4.4.2","PyYAML>=5.3",
                      "requests>=2.22.0","requests-toolbelt>=0.9.1","urllib3>=1.25.8"],
)