# -*- coding: utf-8 -*-
"""
WAVES Jobs client

"""
from .client import CoreClient


class JobClient(CoreClient):

    def __init__(self, base_url, app_key) -> None:
        super().__init__(base_url)
        self.app_key = app_key

    def list(self):
        self.auth_token(self.app_key)
        return self.client.get(self.base_url + "jobs")

    def create(self, service_app_name, submission_app_name="default", inputs={}):
        self.auth_token(self.app_key)
        document = self.client.get(self.base_url + "openapi")
        return self.client.action(document, ["services", "submissions_jobs_create"],
                                  params={
                                      "inputs": inputs,
                                      "name": "Job Name",
                                      "service_app_name": service_app_name,
                                      "submission_app_name": submission_app_name
                                  }, encoding="multipart/form-data")
