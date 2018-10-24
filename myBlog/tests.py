from django.test import TestCase

from .models import Post

# Create your tests here.
class BlogTest(TestCase):
    def testSum(self):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 1 + 1
        # Assert
        self.assertEqual(expected, result)