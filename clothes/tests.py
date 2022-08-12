from django.test import TestCase
from .models import Shirt


class ShirtTest(TestCase):
    """ Test module for Shirt model """

    def setUp(self):
        Shirt.objects.create(
            name='Pena Summer Shirt', size='M', type='T-shirt', color='Black')
        Shirt.objects.create(
            name='Calvin Klein Summer Dyed Shirt', size='G', type='Polo Shirt', color='Brown')

    def test_Shirt_breed(self):
        Shirt_pena = Shirt.objects.get(name='Pena Summer Shirt')
        Shirt_calvin = Shirt.objects.get(name='Calvin Klein Summer Dyed Shirt')
        self.assertEqual(
            Shirt_pena.get_type(), "Pena Summer Shirt is a T-shirt.")
        self.assertEqual(
            Shirt_calvin.get_type(), "Calvin Klein Summer Dyed Shirt is a Polo Shirt.")
