{%- if testing_framework == "unittest" -%}
import unittest

{% endif -%}
from {{package_name}}.{{package_name}} import a_function


{% if testing_framework == "pytest" -%}
def test_a_function():
    assert a_function() == "Hello World!"
{%- elif testing_framework == "unittest" -%}
class TestAFunction(unittest.TestCase):
    def setUp(self):
        pass

    def test_a_function(self):
        result = a_function()

        self.assertEqual("Hello World!", result)

    def tearDown(self):
        pass
{%- endif %}
