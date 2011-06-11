``django-markitup-widget`` is a Django form widget library for using `markItUp! <http://markitup.jaysalvat.com/home/>`_ on Textarea


Install
===========================================
::

	sudo pip install django-markitup-widget

or::

    sudo pip install git+git://github.com/lambdalisue/django-markitup-widget.git#egg=django-markitup-widget

You may need to copy ``templates/markitup`` directory to your ``TEMPLATE_DIRS``

How to Use
==========================================

1.	First, you need to specified ``MARKITUP_PATH`` on ``settings.py``
	``MARKITUP_PATH`` is the URI of markItUp! directory like ``MARKITUP_PATH = r"javascript/markitup"``
2.	Use ``markitup.widgets.MarkItUpTextarea`` widgets for target Textarea like below::
	
		from django import forms
		from markitup.widgets import MarkItUpTextarea

		markitup = MarkItUpTextarea(
			set='default',
			style='simple',
		)
		document = forms.TextField(widget=markitup)

Settings
========================================

``MARKITUP_PATH``
    the URI for markItUp! directory (required)

``MARKITUP_DEFAULT_SET``
	the default set name (DEFAULT: default)

``MARKITUP_DEFAULT_SKIN``
	the default skin name (DEFAULT: simple)
