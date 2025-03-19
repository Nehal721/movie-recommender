from setuptools import setup

with open("README.md", "r", encoding ="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'NEHAL THAKUR'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']
setup(
    name = SRC_REPO,
    version="1.0.0",
    author="Nehal Thakur",
    author_email="nehalthakur_cs24a05_007@dtu.ac.in",
    description="My first ml project-> a small example of movie recommendation system ",
    long_description_content_type="text/markdown",
    url="https://github.com/nehalthakur/movie-recommender",
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)