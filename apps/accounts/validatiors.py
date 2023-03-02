from django.core.validators import RegexValidator


phone_validator: RegexValidator = RegexValidator(
    regex=r'^\+\d{9,20}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 21 digits allowed."
)
