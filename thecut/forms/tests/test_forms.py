# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import forms
from django.test import TestCase
from test_app.forms import (DateClassMixinForm, DateTimeClassMixinForm,
                            EmailTypeMixinForm, MaxLengthMixinForm,
                            PlaceholderMixinForm, RequiredMixinForm,
                            TimeClassMixinForm)
from thecut.forms.forms import DateTimeTimezoneMixin
from mock import patch, MagicMock
from datetime import datetime, tzinfo, timedelta
from django import forms as django_forms
import pytz


class TestEmailTypeMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.EmailTypeMixin` class."""

    def setUp(self):
        self.form = EmailTypeMixinForm()

    def test_input_type_set_to_email_for_emailfield(self):
        """Test that the HTML ``input`` attribute is set to ``email`` on a child
        :py:class:`django.forms.EmailField`."""
        self.assertEqual(self.form.fields['email'].widget.input_type, 'email')

    def test_input_type_not_set_to_email_for_non_emailfield(self):
        """Test that the HTML ``input`` attribute is not set to ``email`` on a
        child :py:class:`django.forms.Field` that is not
        :py:class:`django.forms.EmailField`."""
        self.assertNotEqual(self.form.fields['other'].widget.input_type,
                            'email')


class TestRequiredMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.RequiredMixin` class."""

    def setUp(self):
        self.form = RequiredMixinForm()

    def test_required_attribute_set_for_required_field(self):
        """Test that the HTML5 ``required`` attribute is set on a child
        :py:class:`django.forms.Field` that has ``required`` set to
        ``True``."""
        self.assertIn('required',
                      self.form.fields['required'].widget.attrs.keys())
        self.assertEqual(self.form.fields['required'].widget.attrs['required'],
                         'required')

    def test_required_attribute_not_set_for_optional_field(self):
        """Test that the HTML5 ``required`` attribute is not set on a child
        :py:class:`django.forms.Field` that does not have ``required`` set to
        ``True``."""
        if 'required' in self.form.fields['not_required'].widget.attrs.keys():
            self.assertNotEqual(
                self.form.fields['not_required'].widget.attrs['required'],
                'required')

    def test_required_attribute_not_set_for_required_radio_widget(self):
        """Test that the HTML5 ``required`` attribute is not set on a child
        :py:class:`django.forms.Field` that has ``required`` set to
        ``True`` and uses the :py:class:`django.forms.RadioSelect` widget."""
        if 'required' in self.form.fields['radio'].widget.attrs.keys():
            self.assertNotEqual(
                self.form.fields['radio'].widget.attrs['required'],
                'required')

    def test_required_attribute_not_set_for_required_checkbox_widget(self):
        """Test that the HTML5 ``required`` attribute is not set on a child
        :py:class:`django.forms.Field` that has ``required`` set to
        ``True`` and uses the :py:class:`django.forms.CheckboxSelectMultiple`
        widget."""
        if 'required' in self.form.fields['checkbox'].widget.attrs.keys():
            self.assertNotEqual(
                self.form.fields['checkbox'].widget.attrs['required'],
                'required')


class TestMaxLengthMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.MaxLengthMixin` class."""

    def setUp(self):
        self.form = MaxLengthMixinForm()

    def test_correct_maxlength_set_for_textarea_with_max_length(self):
        """Test if the correct HTML5 ``maxlength`` attribute is set on a
        child :py:class:`django.forms.Field` using
        :py:class:`django.forms.Textarea`and with ``max_length`` set."""
        self.assertIn(
            'maxlength',
            self.form.fields['textarea_max_length'].widget.attrs.keys())
        self.assertEqual(
            self.form.fields['textarea_max_length'].widget.attrs['maxlength'],
            50)

    def test_no_maxlength_for_textarea_with_no_max_length(self):
        """Test if no HTML5 ``maxlength`` attribute is set on a
        child :py:class:`django.forms.Field` using
        :py:class:`django.forms.Textarea` and with no ``max_length`` set."""
        self.assertNotIn('maxlength',
                         self.form.fields['textarea'].widget.attrs.keys())

    def test_no_maxlength_for_non_textarea_with_max_length(self):
        """Test if no HTML5 ``maxlength`` attribute is set on a
        child :py:class:`django.forms.Field` not using
        :py:class:`django.forms.Textarea` but with ``max_length`` set."""
        self.assertNotIn('other_max_length',
                         self.form.fields['textarea'].widget.attrs.keys())

    def test_no_maxlength_for_non_textarea_with_no_max_length(self):
        """Test if no HTML5 ``maxlength`` attribute is set on a
        child :py:class:`django.forms.Field` not using
        :py:class:`django.forms.Textarea` and with no ``max_length`` set."""
        self.assertNotIn('other',
                         self.form.fields['textarea'].widget.attrs.keys())


class TestPlaceholderMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.PlaceholderMixin` class."""

    def setUp(self):
        self.form = PlaceholderMixinForm()

    def test_placeholder_set_when_defiend(self):
        """Test if the correct HTML5 ``placeholder`` attribute is set on a
        field when an appropriate entry is added to the ``placeholders``
        dict."""
        self.assertIn('placeholder', self.form.fields['a'].widget.attrs.keys())
        self.assertEqual(self.form.fields['a'].widget.attrs['placeholder'],
                         'foobar')

    def test_placeholder_not_set_when_not_defiend(self):
        """Test if the correct HTML5 ``placeholder`` attribute is not set on a
        py:class:`django.forms.Field` when no appropriate entry is added to
        the ``placeholders`` dict."""
        self.assertNotIn('placeholder',
                         self.form.fields['b'].widget.attrs.keys())


class TestTimeClassMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.TimeClassMixin` class."""

    def setUp(self):
        self.form = TimeClassMixinForm()

    def test_time_class_added_for_timefield(self):
        """Test if the ``time`` CSS class is applied to a child
        py:class:`django.forms.Field` using the
        :py:class:`django.forms.TimeInput` widget."""
        self.assertIn('time', get_css_classes(self.form.fields['time']))

    def test_time_class_not_added_for_nontimefield(self):
        """Test if the ``time`` CSS class is not applied to a child
        py:class:`django.forms.Field` not using the
        :py:class:`django.forms.TimeInput` widget."""
        self.assertNotIn(
            'time', get_css_classes(self.form.fields['other']))


class TestDateClassMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.DateClassMixin` class."""

    def setUp(self):
        self.form = DateClassMixinForm()

    def test_date_class_added_for_datefield(self):
        """Test if the ``date`` CSS class is applied to a child
        py:class:`django.forms.Field` using the
        :py:class:`django.forms.DateInput` widget."""
        self.assertIn('date', get_css_classes(self.form.fields['date']))

    def test_date_class_not_added_for_nondatefield(self):
        """Test if the ``date`` CSS class is not applied to a child
        py:class:`django.forms.Field` not using the
        :py:class:`django.forms.DateInput` widget."""
        self.assertNotIn(
            'date', get_css_classes(self.form.fields['other']))


class TestDateTimeClassMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.DateTimeClassMixin`
    class."""

    def setUp(self):
        self.form = DateTimeClassMixinForm()

    def test_datetime_class_added_for_datefield(self):
        """Test if the ``datetime`` CSS class is applied to a child
        py:class:`django.forms.Field` using the
        :py:class:`django.forms.DateTimeInput` widget."""
        self.assertIn('datetime', get_css_classes(
            self.form.fields['datetime']))

    def test_datetime_class_added_for_datefield_splitdatetimewidget(self):
        """Test if the ``datetime`` CSS class is applied to a child
        py:class:`django.forms.Field` using the
        :py:class:`django.forms.DateTimeInput` widget."""
        self.assertIn('datetime', get_css_classes(
            self.form.fields['datetime_split']))

    def test_datetime_class_not_added_for_nondatefield(self):
        """Test if the ``datetime`` CSS class is not applied to a child
        py:class:`django.forms.Field` not using the
        :py:class:`django.forms.DateTimeInput` widget."""
        self.assertNotIn(
            'datetime', get_css_classes(self.form.fields['other']))


class TestDateTimeTimezoneMixin(TestCase):

    class UTC(tzinfo):
        """UTC"""

        def utcoffset(self, dt):
            return timedelta(0)

        def tzname(self, dt):
            return 'UTC'

        def dst(self, dt):
            return timedelta(0)

    @patch.object(DateTimeTimezoneMixin, 'initial', create=True)
    @patch.object(DateTimeTimezoneMixin, 'fields', create=True)
    def setUp(self, mock_fields, mock_initial):
        self.mock_target_field = MagicMock()
        self.mock_target_field.widget = \
            django_forms.DateTimeInput()
        mock_other_field = MagicMock()
        mock_other_field.widget.return_value = \
            django_forms.SplitDateTimeWidget()
        mock_fields.return_value = {'target_field': self.mock_target_field,
                                    'other_field': mock_other_field}
        self.form = DateTimeTimezoneMixin()
        self.form.fields = {'target_field': self.mock_target_field,
                            'other_field': mock_other_field}

    def test_setup_timezone_help_texts(self):
        self.form._set_timezone_help_texts({'target_field':
                                           datetime(1990, 1, 1, 0, 0, 0, 0,
                                                    pytz.utc), 'other_field':
                                           datetime(1991, 1, 1, 0, 0, 0)})
        self.assertEqual(self.mock_target_field.help_text, "UTC")


class TestFormMixin(TestCase):

    """Tests for the :py:class:`thecut.forms.forms.EmailTypeMixin` class."""

    def test_inherits_from_emailtypemixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.EmailTypeMixin))

    def test_inherits_from_requiredmixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.RequiredMixin))

    def test_inherits_from_maxlengthmixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.MaxLengthMixin))

    def test_inherits_from_placeholdermixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.PlaceholderMixin))

    def test_inherits_from_timeclassmixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.TimeClassMixin))

    def test_inherits_from_dateclassmixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.DateClassMixin))

    def test_inherits_from_datetimeclassmixin(self):
        self.assertTrue(issubclass(forms.FormMixin, forms.DateTimeClassMixin))


def get_css_classes(field):
    return field.widget.attrs.get('class', '').split()
