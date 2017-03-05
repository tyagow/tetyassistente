from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r

from src.reports.models import Report
from src.testutlis.models import TestBase


class ReportListViewTest(TestBase):
    def setUp(self):
        user = User.objects.create(username='tety', password='123456')
        Report.objects.create(type=1, user=user)
        self.response = self.client.get(r('reports:list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_list.html"""
        self.assertTemplateUsed(self.response, 'reports/report_list.html')

    def test_list_objects_display(self):
        """Must show all Report Objects"""
        expected = ['Alimentação -']
        self.assertContents(expected)


class ReportCreateViewTest(TestBase):
    def setUp(self):
        self.response = self.client.get(r('reports:create'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_form.html"""
        self.assertTemplateUsed(self.response, 'reports/report_form.html')


class ReportDetailViewTest(TestBase):
    def setUp(self):
        user = User.objects.create(username='tety', password='123456')
        Report.objects.create(type=1, user=user)
        self.response = self.client.get(r('reports:detail', pk=1))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_detail.html"""
        self.assertTemplateUsed(self.response, 'reports/report_detail.html')




