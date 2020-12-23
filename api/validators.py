from rest_framework.exceptions import ValidationError


class MyCustomValidator:

    requires_context = True

    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, attrs, serializer):
        request = serializer.context.get('request', None)
        following = attrs.get('following', None)
        if request is None or following is None:
            raise ValidationError('The required data is not available',
                                  code='required_error')
        user = request.user
        if self.queryset.filter(user=user, following=following).exists():
            raise ValidationError('Such object already exists',
                                  code='unique_error')

        if user == following:
            raise ValidationError('It is forbidden to subscribe to yourself',
                                  code='subscribe_error')
