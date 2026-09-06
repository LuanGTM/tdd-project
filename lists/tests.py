from django.test import TestCase
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        table = response.context['table']
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(
                row.text == '1: Estudar testes funcionais'
                for row in rows
            ),
            'New to-do item did not appear in table'
        )