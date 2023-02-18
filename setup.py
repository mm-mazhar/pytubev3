from setuptools import setup, find_packages

setup(
    name = "pytubev3",
    author = "Mazhar",
    author_email = "mazqoty.01@gmail.com",
    maintainer = "Mazhar",
    maintainer_email = "mazqoty.01@gmail.com",
    version = "1.0.0",
    url = "https://github.com/mm-mazhar/pytubev3.git",
    download_url = "https://github.com/mm-mazhar/pytubev3.git",
    project_urls = {"Bug Tracker": "https://github.com/mm-mazhar/pytubev3/issues"},
    keywords = ["Youtube API", "youtube api wrapper", "Python", "Youtube Data API"],
    license = "BSD",
    description = "Python Wrapper of Youtube API", 
    long_description = "Python Wrapper of Youtube API",
    python_requires = ">=3.6",
    include_package_data = True,
    packages = find_packages(),
    install_requires = ["google_api_python_client==2.73.0", 
                        "iteration_utilities==0.11.0", 
                        "setuptools==65.5.0"],
    classifiers = [
        "Environment :: Web Environment",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
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