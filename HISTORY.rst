.. :changelog:

=======
History
=======

0.3.11 (2016-02-28)
-------------------

* Improved unicode support in ``version.py``.
* Added support for rendering honeypot field whilst using the in-built form rendering templates.


0.3.10 (2015-12-09)
-------------------

* Gracefully handle situations where Meta ``placeholders`` attribute does not exist.


0.3.9 (2015-02-24)
------------------

* Created ``PlaceholderMixin`` to allow easy addition of custom placeholder text.
* Added ``PlaceholderMixin`` to ``FormMixin``.


0.3.8 (2015-01-12)
------------------

* Added ``LICENSE``, ``AUTHORS``, ``README``.


0.3.7 (2014-12-12)
------------------

* Bugfix: in form rendering template, render hidden fields.


0.3.6 (2014-12-03)
------------------

* In form rendering template, add class to field ``<li>`` wrapper with input type.


0.3.5 (2014-12-03)
------------------

* Redesigned form rendering template to allow for easier styling.
* Updated ``version.py`` to work with Python 3.


0.3.4 (2014-09-03)
------------------

* Added ``DateTimeTimezoneMixin``.


0.3.3 (2014-06-30)
------------------

* In form rendering templates, separate hidden fields and visible fields.


0.3.2 (2014-04-15)
------------------

* Added missing template files to ``MANIFEST.in``.


0.3.1 (2014-03-19)
------------------

* Added form rendering templates to improve rendering of forms in templates.
* Removed ``distribute`` from application requirements.


0.3 (2014-02-03)
----------------

* Apply HTML5 ``maxlength`` attribute to ``Textarea`` widgets when a maximum length has been specified on the field.


0.2 (2014-01-30)
----------------

* Do not appy ``required`` attribute to certain widgets (``forms.CheckboxSelectMultiple`` or ``forms.RadioSelect``) as the HTML5 ``required`` attribute does not behave correctly on the resulting HTML fields.


0.1 (2013-09-10)
----------------

* Initial release
* Use appropriate HTML5 ``type`` fields for email, time, date, and datetime fields / widgets.
* Apply HTML5 ``required`` attribute to required fields.
