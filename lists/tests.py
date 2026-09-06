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
    def test_can_save_a_POST_request(self):
        response = self.client.post(
            '/',
            data={'item_text': 'A new list item'}
        )
        self.assertIn(
            'A new list item',
            response.content.decode()
        )
        self.assertTemplateUsed(response, 'home.html')