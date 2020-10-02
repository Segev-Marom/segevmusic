import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="segevmusic",
    version="1.0",
    author="Segev Pavin",
    author_email="macsegev@gmail.com",
    description="Downloading with Deezer and tagging with Apple Music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/segevp/music-downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Sound/Audio"
    ],
    python_requires='>=3',
    install_requires=['deemix==1.5.6', 'mutagen']
)