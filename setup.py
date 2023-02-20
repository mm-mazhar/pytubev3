#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the pytubev3"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_Description = f.read()
    
setup(
    name = "pytubev3",
    author = "Mazhar",
    author_email = "mazqoty.01@gmail.com",
    maintainer = "Mazhar",
    maintainer_email = "mazqoty.01@gmail.com",
    version = "1.1.1",
    url = "https://github.com/mm-mazhar/pytubev3.git",
    download_url = "https://github.com/mm-mazhar/pytubev3.git",
    project_urls = {"Bug Tracker": "https://github.com/mm-mazhar/pytubev3/issues"},
    keywords = ["Youtube API", "youtube api wrapper", "Python", "Youtube Data API"],
    license = "BSD",
    description = "Python Wrapper of Youtube API", 
    #long_description = "Python Wrapper of Youtube API",
    long_description = long_Description,
    long_description_content_type = "text/markdown",
    python_requires = ">=3.7",
    include_package_data = True,
    packages = find_packages(),
    install_requires = ["google_api_python_client==2.73.0", 
                        "iteration_utilities==0.11.0", 
                        "setuptools==65.5.0"],
    classifiers = [
        #"Environment :: Web Environment",
        #"Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    # entry_points = {
    #     "console_scripts" : [
    #         "login = lib_work_login.__main__:main",
    #         "configure = lib_work_login.__main__:configure",
    #     ]
    # },
    # setup_requires  = ["pytest-runner"],
    # tests_require = ["pytest"],
    
)