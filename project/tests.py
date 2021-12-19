from django.test import TestCase

# Create your tests here.
from catalog.models import Customer
from owncabinet.models import OwnCabinet
from .models import Project
from django.urls import reverse


class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(company_name='Big Company', foreman_name='Bob Dylan')
        Project.objects.create(customer_id=1, title='Great Project', price=1000.0)

    def test_title_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('title').max_length
        self.assertEquals(max_length, 300)

    def test_get_absolute_url(self):
        project = Project.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(project.get_absolute_url(), '/project/1')

    def test_get_update_url(self):
        project = Project.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(project.get_update_url(), '/project/update/1')

    def test_get_delete_url(self):
        project = Project.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(project.get_delete_url(), '/project/delete/1')


class ProjectListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = OwnCabinet.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Customer.objects.create(company_name='Big Company', foreman_name='Bob Dylan')
        # Create 13 projects for pagination tests
        number_of_projects = 13
        for project_num in range(number_of_projects):
            Project.objects.create(customer_id=1,
                                   title='Title %s' % project_num,
                                   price=1000.0, )

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get('/project/list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('project-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('project-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'project/project_list.html')

    def test_pagination_is_five(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('project-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['project_list']) == 5)

    def test_lists_all_customers(self):
        self.client.login(username='john', password='johnpassword')
        # Get third page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('project-list') + '?page=3')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['project_list']) == 3)


class ProjectDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = OwnCabinet.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Customer.objects.create(company_name='Big Company', foreman_name='Bob Dylan')
        Project.objects.create(customer_id=1, title='Great Project', price=1000.0)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get('/project/1')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('project-detail', args='1'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('project-detail', args='1'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'project/project_detail.html')
