from django.test import TestCase

# Create your tests here.
from collision_data.models import CollisionDetails


class CollisionModelTestCase( TestCase ):

    def setUp(self):
        CollisionDetails.objects.create(bourugh='brookyln', latitude='-4', longitude='4')

    def test_collsionDetails(self ):
        borough = CollisionDetails.objects.get(bourugh='Brooklyn')
        self.assertEqual(latitude='-4')