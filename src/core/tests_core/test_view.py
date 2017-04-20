from unittest import skip

from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:home'))

    def test_get(self):
        self.assertEqual(302, self.response.status_code)

    @skip
    def test_template(self):
        """Must use core/index.html"""
        self.assertTemplateUsed(self.response, 'core/index.html')