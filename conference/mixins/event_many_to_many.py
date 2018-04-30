# -*- coding: utf-8 -*-
"""
Conference relation mixin, to be used in models that are pointing to the
conference.
"""
from django.db import models

from conference.models import Event


class EventMTMMixin:
    """
    A mixin to add to a model which points to a conference.
    """
    class Meta:
        abstract = True

    event = models.ManyToManyField(
        Event,
        help_text="Event to which this belongs. e.g. PyCon 2018.",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
