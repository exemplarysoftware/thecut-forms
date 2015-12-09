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

        # Set HTML5 required attributes. Note that if we set the required
        # attribute on fields with certain widgets, it will cause the form to
        # break by requiring EVERY option to be selected. This is not possible
        # with the RadioSelect widget, and in most cases won't be the desired
        # behaviour with the CheckboxSelectMultiple widget. If it is, the
        # required attribute of the widget can still be set manually in the
        # form.
        for field in self.fields.values():
            if field.required and not (
                    isinstance(field.widget, forms.CheckboxSelectMultiple) or
                    isinstance(field.widget, forms.RadioSelect)):
                field.widget.attrs.update({'required': 'required'})


class MaxLengthMixin(object):
    """Adds the HTML5 'maxlength' attribute to applicable Textarea widgets."""

    def __init__(self, *args, **kwargs):
        super(MaxLengthMixin, self).__init__(*args, **kwargs)

        # HTML5 maxlength attribute for textarea
        for field in self.fields.values():
            if isinstance(field.widget, forms.Textarea) and field.max_length:
                field.widget.attrs.update({'maxlength': field.max_length})


class PlaceholderMixin(object):

    class Meta(object):
        placeholders = {}

    def __init__(self, *args, **kwargs):
        super(PlaceholderMixin, self).__init__(*args, **kwargs)
        for key, value in dict(getattr(self.Meta, 'placeholders', {})).items():
            self.fields[key].widget.attrs.update({'placeholder': value})


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


class DateTimeTimezoneMixin(object):
    """Adds timezone help text to any datetime fields."""

    def __init__(self, *args, **kwargs):
        super(DateTimeTimezoneMixin, self).__init__(*args, **kwargs)
        self._set_timezone_help_texts(data=self.initial)

    def _set_timezone_help_texts(self, data):
        for field_name, field in self.fields.items():
            field_data = data.get(field_name)
            if field_data and isinstance(field.widget, forms.DateTimeInput):
                field.help_text = field_data.tzname()

    def clean(self, *args, **kwargs):
        cleaned_data = super(DateTimeTimezoneMixin, self).clean(*args,
                                                                **kwargs)
        self._set_timezone_help_texts(data=cleaned_data)
        return cleaned_data


class FormMixin(DateTimeClassMixin, DateClassMixin, EmailTypeMixin,
                MaxLengthMixin, PlaceholderMixin, RequiredMixin,
                TimeClassMixin):
    """Form mixin.

    Used to extend a standard Django :py:class:`~django.forms.Form` class with
    useful/common behaviour.

    """

    error_css_class = 'error'
    label_suffix = ''
