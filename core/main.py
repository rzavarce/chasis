"""
    Project: Vertebral, an interface utility to AIOHTTP
    Author: Roger Anibal Zavarce de Armas

    Interfaces manager
"""
# Python Imports
import pathlib

# Vertebral Imports
from vertebral.configs.manager import Manager


from chasis.routes import setup_routes

BASE_PATH = pathlib.Path(__file__).parent.parent


def start():
    """

    :return:
    """
    Manager(BASE_PATH).start(setup_routes())

