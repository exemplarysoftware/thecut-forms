# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from mock import MagicMock
from thecut.forms.utils import add_css_class


class TestAddCssClass(TestCase):
    def test_add_new_css_class(self):
        widget = MagicMock()
        widget.attrs = {'class': 'a b'}
        widget = add_css_class(widget, 'c')
        self.assertEqual(set(widget.attrs.get('class', '').split()),
                         {'a', 'b', 'c'})

    def test_add_existing_css_class(self):
        widget = MagicMock()
        widget.attrs = {'class': 'a b'}
        widget = add_css_class(widget, 'b')
        self.assertEqual(set(widget.attrs.get('class', '').split()),
                         {'a', 'b'})
