# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def add_css_class(widget, css_class):
    css_classes = widget.attrs.get('class', '').split()
    if not css_class in css_classes:
        css_classes.append(css_class)
    widget.attrs.update({'class': ' '.join(css_classes)})
    return widget
