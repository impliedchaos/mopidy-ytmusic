# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["mopidy_ytmusic"]

package_data = {"": ["*"]}

install_requires = [
    "Mopidy>=3,<4",
    "youtube_dl>=2021.1.1,<2022.0.0",
    "ytmusicapi>=0.17.2,<0.18.0",
]

entry_points = {"mopidy.ext": ["ytmusic = mopidy_ytmusic:Extension"]}

setup_kwargs = {
    "name": "mopidy-ytmusic",
    "version": "1.0.10",
    "description": "Mopidy extension for playling music/managing playlists in Youtube Music",
    "long_description": None,
    "author": "Ozymandias (Tomas Ravinskas)",
    "author_email": "tomas.rav@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.7,<4.0",
}


setup(**setup_kwargs)
