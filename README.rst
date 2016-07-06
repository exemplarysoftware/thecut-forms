=======================
Welcome to thecut-forms
=======================


.. image:: https://travis-ci.org/thecut/thecut-forms.svg
    :target: https://travis-ci.org/thecut/thecut-forms

.. image:: https://codecov.io/github/thecut/thecut-forms/coverage.svg
    :target: https://codecov.io/github/thecut/thecut-forms

.. image:: https://readthedocs.org/projects/thecut-forms/badge/?version=latest
    :target: http://thecut-forms.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Form rendering helpers.


Features
--------

* Automatically add appropriate HTML5 ``type``, ``required`` and ``maxlength`` attributes to form fields.
* Automatically add ``date``, ``time``, and ``datetime`` CSS classes to appropriate form fields.
* Easily add custom ``placeholders`` to form fields by editing a ``dict``.
* Easily render forms in your templates in a well-designed standardised way that makes front-end development easier.

Documentation
-------------

The full documentation is at https://thecut-forms.readthedocs.org.


Quickstart
----------

Make sure to install! (:ref:`installation`).

Use one of the many available :py:class:`django.forms.Form` mixins on your :py:class:`django.forms.Form`::

    from django import forms
    from thecut.forms import EmailTypeMixin, TimeClassMixin

    class MyForm(EmailTypeMixin, TimeClassMixin, forms.Form):

        foo = forms.EmailField(required=True)

        bar = forms.TimeField(required=True)

Or use :py:class:`thecut.forms.forms.FormMixin` to get them all at once::

    from django import forms
    from thecut.forms import FormMixin

    class MyForm(FormMixin, forms.Form):

        foo = forms.CharField(required=True)

See :ref:`mixins` for more information.

In your template, use the ``forms/_form.html`` snippet to easily render your forms::

    {% include "forms/_form.html" %}

See :ref:`templates` for more information.


Credits
-------

See :ref:`credits`.
