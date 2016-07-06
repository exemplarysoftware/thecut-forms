=========
Templates
=========

We provide a Django template snippet that can be included in your template files to easily render forms. Among other things, it handles rendering:

- The CSRF token (if required).
- A honeypot field (if required).
- The parent ``<form>`` element.
- Non-field errors.
- Form fields (in a way that makes front-end styling much easier).
- A submit button.


Basuc usage
-----------

In order to render a basic form in your template, just include ```forms/_form.html``::

    {% include "forms/_form.html" %}

You do *not* need to define a ``<form>`` element, call ``{% csrf_token %}``.etc - the snippet will handle this for you.


Customising the form
--------------------

The form template makes use of template context variables to allow you to customise some aspects of its functionality.

==========================  =================================  =========================  ===========================================================================
 Variable                    Description                        Default                    Example
--------------------------  ---------------------------------  -------------------------  ---------------------------------------------------------------------------
 ``form``                    The form to render.                ``form``                   ``{% include "forms/_form.html" with form=my_form %}``
--------------------------  ---------------------------------  -------------------------  ---------------------------------------------------------------------------
 ``form_action``             The URL to post the form to.       ``request.path``           ``{% url 'site:homepage' as my_url %}``
                                                                                           ``{% include "form/_form.html" with form_action=my_url %}``
--------------------------  ---------------------------------  -------------------------  ---------------------------------------------------------------------------
 ``form_method``             The HTTP method to use.            POST                       ``{% include "forms/_form.html" with form_method="GET" %}``
--------------------------  ---------------------------------  -------------------------  ---------------------------------------------------------------------------
 ``form_honeypot_field``     A honeypot field to include in     -                          ``{% include "forms/_form.html" with form_honeypot_field=my_field %}``
                             the form.
--------------------------  ---------------------------------  -------------------------  ---------------------------------------------------------------------------
 ``form_submit_value``       The value (label) for the          Submit                     ``{% include "forms/_form.html" with form_submit_value="Send" %}``
                             form's submit button.
==========================  =================================  =========================  ===========================================================================
