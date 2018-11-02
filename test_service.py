import unittest
from service import Service
from unittest.mock import patch
from unittest import TestCase


class UnitTest(TestCase):


    @patch('service.Service.bad_random')
    def mock_bad_random(self, bad_random_value):
        mock_value = 2
        bad_random_value.return_value = mock_value
        result = Service().bad_random()
        self.assertEqual(result, mock_value)


    @patch('service.Service.bad_random')
    def test_divide(self, bad_random_value):
        bad_random_value.return_value = 20
        assert Service().divide(5) == 4
        assert Service().divide(-5) == -4
        return


    def test_abs_plus(self):
        assert Service().abs_plus(2) == 3
        assert Service().abs_plus(0) == 1
        assert Service().abs_plus(-2) == 3
        return


    @patch('service.Service.bad_random')
    def test_complicated_function(self, bad_random_value):
        mock_value = 20
        bad_random_value.return_value = mock_value
        result = Service().complicated_function(2)
        assert result[0] == 10
        assert result[1] == 0


if __name__ == '__main__':
    unittest.main()
