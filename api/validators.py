from rest_framework.exceptions import ValidationError


class MyCustomValidator:

    requires_context = True

    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, attrs, serializer):
        request = serializer.context.get('request')
        following = attrs.get('following')
        if request is None or following is None:
            raise ValidationError('The required data is not available',
                                  code='required_error')

        if request.user == following:
            raise ValidationError('It is forbidden to subscribe to yourself',
                                  code='subscribe_error')
