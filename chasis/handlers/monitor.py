"""
    Project: Vertebral, an interface utility to AIOHTTP
    Author: Roger Anibal Zavarce de Armas

    Monitor handler
"""

from aiohttp import web


class Monitor(web.View):
    """

    """

    async def post(self) -> web.Response:
        """
        This handler allow to test if the service is up.
        ---
        summary: Monitor System Handler
        tags:
          - Monitor Systems
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                required:
                  - payload
                properties:
                  payload:
                    type: object
        responses:
          '200':
            description: Return a json response with the System Status
            content:
              application/json:
                schema:
                  type: object
                  required:
                    - systems
                  properties:
                    systems:
                      type: object
                      required:
                        - state
                        - message
                      properties:
                        state:
                          type: boolean
                        message:
                          type: string
          '500':
            description: Unknown exception
        """
        payload = await self.request.json()
        response = {
            "key": "json_test",
            "payload": {
                "test": "All Systems are ready...",
                "request": payload
            }
        }
        return web.json_response(response)

    async def get(self) -> web.Response:
        """
        This handler allow to test if the service is up.
        ---
        summary: Monitor System Handler
        tags:
          - Monitor Systems
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                required:
                  - payload
                properties:
                  payload:
                    type: object
        responses:
          '200':
            description: Return a json response with the System Status
            content:
              application/json:
                schema:
                  type: object
                  required:
                    - systems
                  properties:
                    systems:
                      type: object
                      required:
                        - state
                        - message
                      properties:
                        state:
                          type: boolean
                        message:
                          type: string
          '500':
            description: Unknown exception
        """

        # payload = await self.request.json()
        payload = {}

        response = {
            "key": "json_test",
            "payload": {
                "test": "All Systems are ready...",
                "request": payload
            }
        }

        return web.json_response(response)
