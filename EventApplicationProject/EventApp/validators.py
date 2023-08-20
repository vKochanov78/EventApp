import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


def validate_name(value):
    if not re.match("^[A-Za-z]*$", value):
        raise ValidationError(_("The name should contain only letters!"))


def validate_password(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError(_("The password must contain at least 1 digit!"))


def validate_future_date(value):
    if value < datetime.date.today():
        raise ValidationError(_("The date cannot be in the past!"))

