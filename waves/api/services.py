# -*- coding: utf-8 -*-
"""
WAVES Services client

"""
from .client import CoreClient


class SubmissionClient(CoreClient):

    app_name = None
    jobs = []
    inputs = []
    outputs = []

    def __init__(self, base_url) -> None:
        super().__init__(base_url)

    def details(self):
        return self.client.get(self.base_url)

    def inputs(self):
        details = self.details()
        return details['inputs']

    def outputs(self):
        details = self.details()
        return details['outputs']

    def form(self):
        details = self.details()
        return details['form']

    def jobs(self):
        details = self.details()
        return details['jobs']


class ServiceClient(CoreClient):

    def __init__(self, base_url) -> None:
        super().__init__(base_url)

    def list(self):
        print(self.base_url + "schema")
        services = self.client.get(self.base_url + "schema")
        return self.client.action(services, ["services", "list"])

    def details(self, app_name):
        print(self.base_url + "services/" + app_name)
        service_details = self.client.get(self.base_url + "services/" + app_name)
        return service_details

    def submissions(self, app_name):
        details = self.details(app_name)
        submissions = []
        for sub in details['submissions']:
            submissions.append(SubmissionClient(sub['url']))
        return submissions

    def submission(self, app_name, submission_app_name):
        submission = SubmissionClient(self.base_url, app_name)
        return submission.details(submission_app_name)
