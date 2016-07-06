===========
Form Mixins
===========

The following mixins can be applied to any :py:class:`~django.forms.Form`-type object.


``EmailTypeMixin``
------------------

.. autoclass:: thecut.forms.forms.EmailTypeMixin
  :members:


``RequiredMixin``
------------------

.. autoclass:: thecut.forms.forms.RequiredMixin
  :members:


``MaxLengthMixin``
------------------

.. autoclass:: thecut.forms.forms.MaxLengthMixin
  :members:


``PlaceholderMixin``
--------------------

.. autoclass:: thecut.forms.forms.PlaceholderMixin
  :members:


``TimeClassMixin``
------------------

.. autoclass:: thecut.forms.forms.TimeClassMixin
  :members:


``DateClassMixin``
------------------

.. autoclass:: thecut.forms.forms.DateClassMixin
  :members:


``DateTimeClassMixin``
----------------------

.. autoclass:: thecut.forms.forms.DateTimeClassMixin
  :members:


``FormMixin``
-------------

In order to make it easy to use all of the above mixins, we have provided
:py:class:`thecut.forms.forms.FormMixin` which inherits from all other mixins.

.. autoclass:: thecut.forms.forms.FormMixin
  :members:
  :show-inheritance:
  :inherited-members:
