# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from thecut.forms.forms import (DateClassMixin, DateTimeClassMixin,
                                EmailTypeMixin, MaxLengthMixin,
                                PlaceholderMixin, RequiredMixin,
                                TimeClassMixin)


class EmailTypeMixinForm(EmailTypeMixin, forms.Form):

    email = forms.EmailField()

    other = forms.CharField()


class RequiredMixinForm(RequiredMixin, forms.Form):

    required = forms.CharField(required=True)

    not_required = forms.CharField(required=False)

    radio = forms.ChoiceField(required=True,
                              choices=(('A', 'A'), ('B', 'B')),
                              widget=forms.RadioSelect)
    checkbox = forms.MultipleChoiceField(required=True,
                                         choices=(('A', 'A'), ('B', 'B')),
                                         widget=forms.CheckboxSelectMultiple)


class MaxLengthMixinForm(MaxLengthMixin, forms.Form):

    textarea = forms.CharField(widget=forms.Textarea)

    textarea_max_length = forms.CharField(max_length=50,
                                          widget=forms.Textarea)

    other = forms.CharField(widget=forms.TextInput)

    other_max_length = forms.CharField(max_length=50,
                                       widget=forms.TextInput)


class PlaceholderMixinForm(PlaceholderMixin, forms.Form):

    a = forms.CharField()

    b = forms.CharField()

    class Meta(object):

        placeholders = {
            'a': 'foobar'
        }


class TimeClassMixinForm(TimeClassMixin, forms.Form):

    time = forms.TimeField()

    other = forms.CharField()


class DateClassMixinForm(DateClassMixin, forms.Form):

    date = forms.DateField()

    other = forms.CharField()


class DateTimeClassMixinForm(DateTimeClassMixin, forms.Form):

    datetime = forms.DateTimeField()

    other = forms.CharField()
