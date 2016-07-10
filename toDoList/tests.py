from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
from toDoList.models import Task


class TestTodo(TestCase):

	def setUp(self):

		testuser = User.objects.create(username='testuser')
		onetodo = Task.objects.create(user=testuser)
		onetodo.title = 'testtitle'
		onetodo.description = 'testdescription'
		onetodo.priority = 'A'
		onetodo.is_completed = False
		onetodo.save()


	def test_model(self):

		self.assertEquals(Task.objects.count(), 1)
		objectindb = Task.objects.get()
		self.assertEquals(objectindb.title, 'testtitle')



















# class MySeleniumTests(StaticLiveServerTestCase):
#     fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         super(MySeleniumTests, cls).setUpClass()
#         cls.selenium = WebDriver()

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(MySeleniumTests, cls).tearDownClass()

#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('admin')
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('qwe123qwe')
#         self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()