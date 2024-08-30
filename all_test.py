from unittest import TestCase, main

from store_scripts import Product, DBScript, Order

class TestOrder(TestCase):
    def test_valid_checkout_form_is_correct(self):
        self.assertEqual(Order.valid_checkout_form('0789888891', 'II Plateaux Adjein'), 'success_valid_checkout_form')
        self.assertEqual(Order.valid_checkout_form(int('0789888891'), 'II Plateaux Adjein'), 'success_valid_checkout_form')
    def test_valid_checkout_form_if_not_phone_number(self):
        self.assertEqual(Order.valid_checkout_form('Bonjour', 'II Plateaux Adjein'), 'user_phone_number_not_int')

if __name__ == '__main__':
    main()