# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from thecut.forms.utils import add_css_class


class EmailTypeMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that sets the HTML5
    ``email`` input type on any child :py:class:`~django.forms.EmailField`
    instances."""

    def __init__(self, *args, **kwargs):
        super(EmailTypeMixin, self).__init__(*args, **kwargs)

        # Set HTML5 input type for email fields
        for field in self.fields.values():
            if isinstance(field, forms.EmailField):
                field.widget.input_type = 'email'


class RequiredMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that sets the HTML5
    ``required`` attribute on any child :py:class:`~django.forms.Field`
    instances that is required.

    This mixin does not apply the `required` attribute to fields using
    :py:class:`~django.forms.RadioSelect` and
    :py:class:`~django.forms.CheckboxSelectMultiple` as
    the HTML5 ``required`` attribute does not behave as (usually) expected on
    these widgets.
    """

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
    """A mixin for a :py:class:`~django.forms.Form` that sets the HTML5
    ``maxlength`` attribute on any child :py:class:`~django.forms.Field`
    instances using the :py:class:`~django.forms.Textarea` widget.

    A ``max_length`` must be specified on the :py:class:`~django.forms.Field`.
    """
    def __init__(self, *args, **kwargs):
        super(MaxLengthMixin, self).__init__(*args, **kwargs)

        # HTML5 maxlength attribute for textarea
        for field in self.fields.values():
            if isinstance(field.widget, forms.Textarea) and field.max_length:
                field.widget.attrs.update({'maxlength': field.max_length})


class PlaceholderMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that allows you to easily set
    the HTML5 ``placeholder`` widget on a child
    :py:class:`~django.forms.Field`.

    To add a ``placeholder`` to a :py:class:`~django.forms.Field`, specify it
    in a ``placeholders`` ``dict`` on the :py:class:`~django.forms.Form`'s
    :py:class:`~django.forms.Form.Meta` class. For example::

        class MyForm(forms.Form):

            foo = forms.CharField()

            class Meta(object):
                placeholders = {
                    'foo': 'Enter some text here.'
                }
    """

    class Meta(object):
        placeholders = {}

    def __init__(self, *args, **kwargs):
        super(PlaceholderMixin, self).__init__(*args, **kwargs)
        for key, value in dict(getattr(self.Meta, 'placeholders', {})).items():
            self.fields[key].widget.attrs.update({'placeholder': value})


class TimeClassMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that adds a ``time`` CSS
    class on any child :py:class:`~django.forms.Field` instances using the
    :py:class:`~django.forms.TimeInput` widget.."""

    def __init__(self, *args, **kwargs):
        super(TimeClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, forms.TimeInput):
                add_css_class(field.widget, 'time')


class DateClassMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that adds a ``date`` CSS
    class on any child :py:class:`~django.forms.Field` instances using the
    :py:class:`~django.forms.DateInput` widget.."""

    def __init__(self, *args, **kwargs):
        super(DateClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, forms.DateInput):
                add_css_class(field.widget, 'date')


class DateTimeClassMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that adds a ``datetime`` CSS
    class on any child :py:class:`~django.forms.Field` instances using the
    :py:class:`~django.forms.DateTimeInput` widget.."""

    def __init__(self, *args, **kwargs):
        super(DateTimeClassMixin, self).__init__(*args, **kwargs)

        # HTML5 input types and attributes
        for field in self.fields.values():
            if isinstance(field.widget, (forms.DateTimeInput,
                                         forms.SplitDateTimeWidget)):
                add_css_class(field.widget, 'datetime')


class DateTimeTimezoneMixin(object):
    """A mixin for a :py:class:`~django.forms.Form` that adds ``help_text``
    to any child :py:class:`~django.forms.Field` instances using the
    :py:class:`~django.forms.DateTimeInput` widget.

    This help text contains the timezone for the field's recorded data (if
    any)).
    """

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
