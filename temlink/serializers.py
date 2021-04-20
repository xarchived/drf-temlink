from rest_framework import fields, serializers


# noinspection PyAbstractClass
class LinkSerializer(serializers.Serializer):
    METHOD_CHOICES = (
        'GET',
        'POST',
        'PUT',
        'DELETE',
        'OPTIONS',
        'PATCH',
    )

    method = fields.ChoiceField(choices=METHOD_CHOICES, required=True)
    url = fields.URLField(required=True)
    body = fields.JSONField(required=False)
