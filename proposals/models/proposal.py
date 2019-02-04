from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

from conference.mixins.event_foreign_key import EventFKMixin
from presenters.models import Presenter


class Proposal(EventFKMixin):

    PROPOSAL_PENDING = 0
    PROPOSAL_ACCEPTED = 1
    PROPOSAL_REJECTED = 2

    PROPOSAL_STATE = (
        (PROPOSAL_PENDING, _('Pending for approval')),
        (PROPOSAL_ACCEPTED, _('Approved')),
        (PROPOSAL_REJECTED, _('Rejected'))
    )

    PROPOSAL_TYPE_WORKSHOP = 0
    PROPOSAL_TYPE_PRESENTATION = 1

    PROPOSAL_TYPE = (
        (PROPOSAL_TYPE_WORKSHOP, _('Workshop')),
        (PROPOSAL_TYPE_PRESENTATION, _('Presentation'))
    )

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        help_text=_('Issuer of the proposal'),
        on_delete=models.SET_NULL
    )

    title = models.CharField(
        max_length=1024,
        help_text=_('Title of Proposal'),
    )

    state = models.IntegerField(
        choices=PROPOSAL_STATE,
        default=PROPOSAL_PENDING,
        help_text=_('Current state of proposal')
    )

    type = models.IntegerField(
        choices=PROPOSAL_TYPE,
        help_text=_('Type of proposal')
    )

    duration = models.IntegerField(
        help_text=_('Estimated duration (minutes)')
    )

    short_description = RichTextField(
        help_text=_('Short information about proposal')
    )

    extra_info = RichTextField(
        help_text=_('Extra information'),
        blank=True,
        null=True
    )
    # Presenter also links to user, which causes denormalization as this model
    # also has a foreign key to user, but I think that connection to the user
    # should be through a Presenter model because if someone uploads a proposal
    # they become potential presenters and it's ok to have their data. Only
    # they shouldn't be shown then if their presentations are not confirmed.
    presenter = models.ForeignKey(
        Presenter,
        help_text=_('Foreign key to presenter who proposed this '
                    'talk/workshop'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __repr__(self):
        return '<Proposal type: {0} state: {1} by: {2}>'.format(
                    self.type,
                    self.state,
                    self.user
                )

    def __str__(self):
        return self.title
