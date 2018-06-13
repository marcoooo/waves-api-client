# -*- coding: utf-8 -*-
"""
Base Api Client
TODO: integrate OpenApiCodec
"""
from coreapi import Client, auth
from coreapi.codecs import JSONCodec
from openapi_codec import OpenAPICodec

class CoreClient(object):
    decoders = [OpenAPICodec(), JSONCodec()]

    def __init__(self, base_url) -> None:
        super().__init__()
        self.base_url = base_url
        self.client = Client(decoders=self.decoders)

    def auth_token(self, app_key):
        self.client = Client(
            auth=auth.TokenAuthentication(token=app_key, scheme="Token"),
            decoders=self.decoders)
