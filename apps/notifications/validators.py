from django.core.validators import RegexValidator


push_template_validator: RegexValidator = RegexValidator(
    regex=r'{order_id}|{order_sum}|{order_currency}|{order_status}',
    message='Template must contain at least one of the following parameters in curly brackets: '
            'order_id, order_sum, order_currency, order_status.'
)
