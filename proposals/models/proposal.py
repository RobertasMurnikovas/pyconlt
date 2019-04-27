import bleach
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Avg
from django.utils.translation import ugettext_lazy as _

from conference.mixins.event_foreign_key import EventFKMixin
from presenters.models import Presenter
from .review import Review


class Proposal(EventFKMixin):

    PROPOSAL_PENDING = 0
    PROPOSAL_ACCEPTED = 1
    PROPOSAL_REJECTED = 2
    PROPOSAL_CANCELLED = 3

    PROPOSAL_STATE = (
        (PROPOSAL_PENDING, _('Pending for approval')),
        (PROPOSAL_ACCEPTED, _('Approved')),
        (PROPOSAL_REJECTED, _('Rejected')),
        (PROPOSAL_CANCELLED, _('Cancelled'))
    )

    PROPOSAL_TYPE_WORKSHOP = 0
    PROPOSAL_TYPE_PRESENTATION = 1

    PROPOSAL_TYPE = (
        (PROPOSAL_TYPE_WORKSHOP, _('Workshop')),
        (PROPOSAL_TYPE_PRESENTATION, _('Presentation'))
    )

    AUDIENCE_JUNIOR = 0
    AUDIENCE_INTERMEDIATE = 1
    AUDIENCE_EXPERT = 2
    AUDIENCE_EXPERIENCE = (
        (AUDIENCE_JUNIOR, _('Junior')),
        (AUDIENCE_INTERMEDIATE, _('Intermediate')),
        (AUDIENCE_EXPERT, _('Expert'))
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

    audience_experience = models.IntegerField(
        choices=AUDIENCE_EXPERIENCE,
        default=AUDIENCE_JUNIOR,
        help_text=_('Audience level')
    )

    target_audience = RichTextField(
        help_text=_('Target audience'),
        blank=True,
        null=True
    )

    speaker_grant = models.BooleanField(
        help_text=_('Check if you need a speaker grant'),
        default=False
    )

    grant_description = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        help_text=_(
            'Short description about travel expenses or expected grant amount')
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

    # Proposal or Talk tags ex.: "DevOps, WebDev.."
    tags = ArrayField(
        models.CharField(
            max_length=50,
            blank=True,
            null=True
        ),
        help_text=_("Proposal/Talk tags"),
        blank=True,
        null=True
    )

    def get_review_rating(self):
        rating = Review.objects.filter(
            proposal=self.pk,
            rating__isnull=False
            ).aggregate(Avg('rating')).get('rating__avg', None)

        return format(rating, '.2f') if rating else "No rating"

    def __repr__(self):
        return '<Proposal type: {0} state: {1} by: {2}>'.format(
                    self.type,
                    self.state,
                    self.user
                )

    def __str__(self):
        return self.title or "No title"

    def clean(self):
        super(Proposal, self).clean()

        self.short_description = bleach.clean(self.short_description)
        self.extra_info = bleach.clean(self.extra_info)
        self.target_audience = bleach.clean(self.target_audience)
