#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/18
#
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.safestring import mark_safe
from django.core.exceptions import ImproperlyConfigured

# check is configured correctly
if not hasattr(settings, "MARKITUP_PATH"):
    raise ImproperlyConfigured("You must define the MARKITUP_PATH before using the MarkItUpTextarea.")

if settings.MARKITUP_PATH.endswith('/'):
    settings.MARKITUP_PATH = settings.MARKITUP_PATH[:-1]
    
# set default settings
settings.MARKITUP_DEFAULT_SET  = getattr(settings, 'MARKITUP_DEFAULT_SET', 'default')
settings.MARKITUP_DEFAULT_SKIN  = getattr(settings, 'MARKITUP_DEFAULT_SKIN', 'simple')

class MarkItUpTextarea(forms.Textarea):
    u"""Textarea widget render with `markItUp`
    
    markItUp:
        http://markitup.jaysalvat.com/home/
    """
    def __init__(self, attrs=None, path=None, set=None, skin=None, **kwargs):
        u"""Constructor of MarkItUpTextarea
        
        Attributes:
            path        - MarkItUp directory URI (DEFAULT = settings.MARKITUP_PATH)
            set         - MarkItUp set name
            skin        - MarkItUp skin name
        
        Example:
            *------------------------------------------*
            + javascript
              + markitup
                + sets
                  + default
                    + set.js
                    + style.css
                + skins
                  + simple
                    + style.css
              + jquery.markitup.js
            *------------------------------------------*
            settings.MARKITUP_PATH = r"javascript/markitup"
            
            markitup = MarkItUpTextarea(
                set='default', skin='simple'
            )
            document = forms.TextField(widget=markitup)
        """
        super(MarkItUpTextarea, self).__init__(attrs=attrs, **kwargs)
        self.path = path or settings.MARKITUP_PATH
        self.set = set or settings.MARKITUP_DEFAULT_SET
        self.skin = skin or settings.MARKITUP_DEFAULT_SKIN
    
    @property
    def media(self):
        css = {
            'screen, projection': (
                r"%s/sets/%s/style.css" % (self.path, self.set),
                r"%s/skins/%s/style.css" % (self.path, self.skin),
            )
        }
        js = (
            r"%s/jquery.markitup.js" % self.path,
            r"%s/sets/%s/set.js" % (self.path, self.set)
        )
        return forms.Media(css=css, js=js)
    
    def render(self, name, value, attrs=None):
        u"""Render MarkItUpTextarea"""
        html = super(MarkItUpTextarea, self).render(name, value, attrs)
        code = render_to_string('markitup/javascript.html', {'id': 'id_%s'%name})
        body = "%s\n%s" % (html, code)
        return mark_safe(body)

class AdminMarkItUpTextareaWidget(MarkItUpTextarea, AdminTextareaWidget):
    pass
