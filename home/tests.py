from django.test import TestCase
from .models import Photo, Image
# Create your tests here.


class PhotoTestClass(TestCase):
    def setUp(self):
        self.new_photo = Photo(file='new_url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo, Photo))


class ImageClass(TestCase):
    def setUp(self):
        self.image = Image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
