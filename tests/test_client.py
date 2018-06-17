# -*- coding: utf-8 -*-

"""
Test basics services
@author
TODO: add mock to work offline
"""
import unittest

from os.path import dirname, join
from waves.api.services import ServiceClient
from waves.api.jobs import JobClient
from coreapi.utils import File


class TestClients(unittest.TestCase):

    def testServices(self):
        self.assertTrue(True)
        serviceClient = ServiceClient("http://127.0.0.1:8000/api/")
        services = serviceClient.list()
        self.assertGreater(len(services), 0)
        serv1 = services[0]
        details = serviceClient.details(serv1['service_app_name'])
        submissions = serviceClient.submissions(serv1['service_app_name'])
        self.assertIsNotNone(submissions[0].details())
        subdetails = submissions[0].details()
        self.assertIsNotNone(subdetails)
        jobclient = JobClient(base_url="http://127.0.0.1:8000/api/", app_key="411874c8ad92e52918df13908c168e9368b33183")
        self.assertIsNotNone(jobclient.list())
        with open(join(dirname(__file__), "test.txt"), 'r') as f:
            new_job = jobclient.create(service_app_name='service_1', submission_app_name="default",
                                       inputs={"dir": "/home/", "file": File("test.txt", f)})
        print(new_job)
