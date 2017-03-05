from django.test import TestCase


class TestBase(TestCase):

    """Test base Have assertContent method for easy test multiple contents"""

    def assertContents(self, contents):
        for expected_content in contents:
            with self.subTest():
                self.assertContains(self.response, expected_content)