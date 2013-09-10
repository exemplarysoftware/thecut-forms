# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from thecut.forms.utils import add_css_class


class EmailTypeMixin(object):
    """Adds the HTML5 'email' input type to any email fields."""

    def __init__(self, *args, **kwargs):
        super(EmailTypeMixin, self).__init__(*args, **kwargs)

        # Set HTML5 input type for email fields
        for field in self.fields.values():
            if isinstance(field, forms.EmailField):
                field.widget.input_type = 'email'


class RequiredMixin(object):
    """Adds the HTML5 'required' attribute to any required fields."""

    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(RequiredMixin, self).__init__(*args, **kwargs)

        # HTML5 required attributes
        for field in self.fields.values():
            if field.required:
                field.widget.attrs.update({'required': 'required'})


class TimeClassMixin(object):
    """Adds a 'time' css class to any time fields."""

    def __init__(self, *args, **kwargs):
        super(TimeClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, forms.TimeInput):
                add_css_class(field.widget, 'time')


class DateClassMixin(object):
    """Adds a 'date' css class to any date fields."""

    def __init__(self, *args, **kwargs):
        super(DateClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, forms.DateInput):
                add_css_class(field.widget, 'date')


class DateTimeClassMixin(object):
    """Adds a 'datetime' css class to any datetime fields."""

    def __init__(self, *args, **kwargs):
        super(DateTimeClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, forms.DateTimeInput):
                add_css_class(field.widget, 'datetime')


class FormMixin(DateTimeClassMixin, DateClassMixin, TimeClassMixin,
                EmailTypeMixin, RequiredMixin):
    """Form mixin.

    Used to extend a standard Django :py:class:`~django.forms.Form` class with
    useful/common behaviour.

    """

    error_css_class = 'error'
    label_suffix = ''
