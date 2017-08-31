import datetime

from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r, render
from django.test import RequestFactory
from django.urls import reverse
from django.utils import timezone

from src.core.tests_core.factory import UserFactory
from src.reports.models import Report
from src.reports.views import ReportCreateView
from src.testutlis.utils import TestBase


class ReportListViewTest(TestBase):
    def setUp(self):
        user = User.objects.create_user(username='tety', password='123456')
        user_lost = User.objects.create_user(username='lost', password='123456')
        self.report = Report.objects.create(user=user, content='Conteudo User user')
        Report.objects.create(user=user_lost, content='Conteudo User lost')
        self.client.login(username='tety', password='123456')
        self.response = self.client.get(r('reports:list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_list.html"""
        self.assertTemplateUsed(self.response, 'reports/report_list.html')

    def test_list_objects_display_only_from_user(self):
        """Must show all Report Objects from the request.user"""
        expected = ['Como estou me sentido? - Conteudo User user']
        self.assertContents(expected)
        self.assertNotContains(self.response, 'Conteudo User lost')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(r('reports:list'))
        self.assertEqual(response.status_code, 302)


class ReportCreateViewTest(TestBase):
    def setUp(self):
        self.factory = RequestFactory()
        user = User.objects.create_user(username='tety', password='123456')
        self.client.login(username='tety', password='123456')
        self.response = self.client.get(r('reports:create'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_form.html"""
        self.assertTemplateUsed(self.response, 'reports/report_form.html')

    def test_login_required(self):
        self.client.logout()
        self.response = self.client.get(r('reports:list'))
        self.assertEqual(self.response.status_code, 302)

    # def test_post_valid_data(self):
    #     self.response = self.client.post(r('reports:create'), data=)

    # @patch('src.reports.models.Report.save', MagicMock(name="save"))
    def test_post(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'type': 1,
            'timestamp': (timezone.now()-datetime.timedelta(hours=3)).strftime("%d/%m/%Y - %H:%M "),
            'content': 'Teste conteudo',

        }
        self.user = UserFactory()

        request = self.factory.post(reverse('reports:create'), data)
        request.user = self.user
        # Get the response
        response = ReportCreateView.as_view()(request)
        # print(response.)
        # self.assertEqual(response.status_code, 302)
        # Check save was called
        # print(render(response, 'reports/report_form.html').content)
        # self.assertTrue(Report.objects.exists())
        # self.assertEqual(Report.objects.count(), 1)


class ReportDetailViewTest(TestBase):
    def setUp(self):
        user = User.objects.create_user(username='tety', password='123456')
        Report.objects.create(type=1, user=user)
        self.client.login(username='tety', password='123456')
        self.response = self.client.get(r('reports:detail', pk=1))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use reports/report_detail.html"""
        self.assertTemplateUsed(self.response, 'reports/report_detail.html')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(r('reports:list'))
        self.assertEqual(response.status_code, 302)



