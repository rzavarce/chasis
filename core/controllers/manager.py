"""
    Project: Vertebral, an interface utility to AIOHTTP
    Author: Roger Anibal Zavarce de Armas

    Web Application Manager
"""
# Python Imports
import pathlib
import aioreloader
from aiohttp import web

# Vertebral Imports
from vertebral.configs.env_vars import EnvironmentVars
from vertebral.configs.yaml import ConfigSetter
from vertebral.configs.logger import LoggerSetter
from vertebral.configs.swagger import SwaggerSetter
from vertebral.configs.routes import Router

from chasis.routes import setup_routes


class Manager:
    """

    # TODO POSIBLEMENTE ESTA CLASE SEA MEJOR MOVEZZ PARA VERTEBRAL
    """

    def __init__(self):
        """

        """
        self.logger = None
        self.swagger = None
        self.router = None
        self.app = web.Application()
        aioreloader.start()

    def start(self):
        """

        :return:
        """
        self.set_logger()
        self.set_env_vars()
        self.set_configs()
        self.set_swagger()
        self.load_routes()
        self.show_ok_message()
        web.run_app(self.app)

    def set_logger(self):
        """

        :return:
        """
        self.logger = self.app['logger'] = LoggerSetter().set_logger()
        self.logger.info("Logger has been loaded")

    def set_env_vars(self):
        """

        :return:
        """
        env = EnvironmentVars()
        self.app['env'] = env.vars
        self.logger.info("Environments Vars has been loaded")

    def set_configs(self):
        """

        :return:
        """
        base_path = pathlib.Path(__file__).parent.parent.parent
        config_path = base_path / "config/config.yml"
        config = ConfigSetter(config_path)
        self.app['config'] = config.settings
        self.logger.info("Config File has been loaded", extra={'path': config_path})

    def set_swagger(self):
        """

        :return:
        """
        swagger = SwaggerSetter(self.app)
        swagger.validate = self.app['config']['swagger']["enabled"]
        self.swagger = swagger.set_swagger(self.app['config']['swagger'])
        self.logger.info("Swagger/Openapi has been setter", extra={'swagger_routes': self.swagger})

    def load_routes(self):
        """

        :return:
        """
        self.router = Router(self.swagger)
        self.router.load_routes(setup_routes())
        self.logger.info("Routes has been loaded", extra={'router': self.router})

    def show_ok_message(self):
        """

        :return:
        """
        msg = {
            "host": self.app['config']["host"],
            "port": self.app['config']["port"],
            "app_name": self.app['config']["app_name"],
            "version": self.app['config']["version"],
        }
        self.logger.info("All Systems are ready", extra=msg)






