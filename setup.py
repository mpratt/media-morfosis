import os
from setuptools import setup, find_packages

DEPENDENCIES = ( 'ffmpeg-python', 'alive_progress' )

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'media-morfosis',
    version = '0.1.0',
    author = "Michael Pratt",
    author_email = "author@michaelpratt.dev",
    description = ( "Converts media files into other formats" ),
    license = "MIT",
    keywords = "",
    url = "",
    packages = find_packages(),
    package_dir = { '' : 'src' },
    long_description = read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=DEPENDENCIES,
    entry_points = {
        'console_scripts': [
            'media-morfosis = media_morfosis.gui:run_gui',
            'media-morfosis-cli = media_morfosis.cli:run',
        ],
    },
)
