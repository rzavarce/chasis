"""
    Project: Vertebral, an interface utility to AIOHTTP
    Author: Roger Anibal Zavarce de Armas

    Routes descriptor
"""

# Projects Imports
from .handlers.monitor import (
    Monitor,
)


def setup_routes() -> list:
    """
    Register existing routes in the app instance.
    :params: application instance
    """

    return [
        ["*", "monitor", Monitor],
        # ["get", "monitor", MonitorGetHandler],
    ]
