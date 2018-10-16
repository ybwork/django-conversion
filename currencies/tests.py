from django.test import TestCase
from django.urls import reverse

from currencies import views as currencies_views
from currencies import utils as currencies_utils


class CurrencyMethodTests(TestCase):
    def test_home_page_if_no_currencies(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_convert_currency_if_not_valid_data(self):
        response = self.client.get(reverse('currency_convert'))
        self.assertEqual(response.status_code, 400)

    def test_http404_if_currency_rates_does_not_exists(self):
        response = self.client.get(
            reverse('currency_convert'),
            {'from_currency': 0, 'to_currency': 2, 'amount': 1}
        )
        self.assertEqual(response.status_code, 404)

    def test_correct_count_money(self):
        amount = 10
        cost = 0.8
        result = round(amount * cost, 2)
        self.assertEqual(currencies_views.count_money(amount, cost), result)

    def test_get_rates_from_api_if_not_valid_params(self):
        base_currency = 'ddfdf'
        self.assertEqual(currencies_utils.get_currency_rates_from_api(base_currency), 400)


