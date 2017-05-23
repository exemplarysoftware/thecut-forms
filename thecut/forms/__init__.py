# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

try:
    from .forms import FormMixin
except ImportError:
    pass

__title__ = 'thecut-forms'

__version__ = '0.5'

__url__ = 'https://github.com/thecut/thecut-forms'

__author__ = 'The Cut Creative <development@thecut.net.au>'

__copyright__ = 'Copyright 2013-2017 Busara Perth Pty Ltd'

__license__ = 'Apache 2.0'

default_app_config = 'thecut.forms.apps.AppConfig'
