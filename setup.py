from setuptools import setup, find_packages


VERSION = '0.0.5'
DESCRIPTION = 'Download Comics from Getcomics.info'

# Setting up
setup(
    name="getdownloader",
    version=VERSION,
    author="Jupie (Faseeh Shahzad Memon)",
    author_email="<faseehshahzad2@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["bs4","colorama","requests","os","re"],    # need to update accordingly
    keywords=['python', 'comic', 'download', 'downloader', 'comic downloader', 'comics downloader'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)