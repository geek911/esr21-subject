from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from django.utils.safestring import mark_safe

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import CellNumber, TelephoneNumber
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin


class SubjectLocator(NonUniqueSubjectIdentifierFieldMixin,
                     SiteModelMixin, BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,)

    date_signed = models.DateField(
        verbose_name='Date Locator form signed',
        default=get_utcnow,)

    permission = models.CharField(
        verbose_name='Has the participant given his/her permission for study '
                     'staff to make home visits for follow-up purposes during '
                     'the study?',
        max_length=5,
        choices=YES_NO, )

    physical_address = models.CharField(
        verbose_name='Physical address with detailed description',
        max_length=50,
        null=True,
        blank=True,)

    call_permission = models.CharField(
        verbose_name='Has the participant given his/her permission for '
                     'study staff to call her for follow-up purposes '
                     'during the study?',
        max_length=5,
        choices=YES_NO, )

    participant_cell = EncryptedCharField(
        verbose_name="Cell number",
        max_length=8,
        validators=[CellNumber, ],
        blank=True,
        null=True)

    alt_participant_cell = EncryptedCharField(
        verbose_name="Cell number (alternative)",
        max_length=8,
        validators=[CellNumber, ],
        blank=True,
        null=True)

    participant_tel = EncryptedCharField(
        verbose_name="Telephone number",
        max_length=8,
        validators=[TelephoneNumber, ],
        blank=True,
        null=True)

    alt_participant_tel = EncryptedCharField(
        verbose_name="Telephone (alternative)",
        max_length=8,
        validators=[TelephoneNumber, ],
        blank=True,
        null=True)

    may_call_work = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        verbose_name=mark_safe(
            'Has the participant given his/her permission for study staff '
            'to contact her at work for follow up purposes during the study?'))

    work_place = models.CharField(
        verbose_name='Name of work place',
        max_length=20,
        null=True,
        blank=True)

    work_location = models.CharField(
        verbose_name='Location of work place',
        max_length=20,
        null=True,
        blank=True)

    work_tel = EncryptedCharField(
        verbose_name="Work contact number",
        max_length=8,
        validators=[TelephoneNumber, ],
        blank=True,
        null=True)

    call_any = models.CharField(
        verbose_name='Has the participant given permission for study'
                     'staff to contact anyone else for follow-up purposes'
                     ' during the study?',
        max_length=5,
        choices=YES_NO, )

    full_name = EncryptedCharField(
        verbose_name="Full names of contact person",
        max_length=35,
        help_text="include firstname and surname",
        blank=True,
        null=True)

    relation_to_participant = models.CharField(
        verbose_name="Relationship to participant",
        max_length=35,
        blank=True,
        null=True)

    address = models.CharField(
        verbose_name='Full physical address',
        max_length=50,
        null=True,
        blank=True, )

    cell = EncryptedCharField(
        verbose_name="Cell number",
        max_length=8,
        validators=[CellNumber, ],
        blank=True,
        null=True)

    tel = EncryptedCharField(
        verbose_name="Telephone number",
        max_length=8,
        validators=[TelephoneNumber, ],
        blank=True,
        null=True)

    class Meta:
        verbose_name = "Subject Locator"
        verbose_name_plural = "Subject Locator"
