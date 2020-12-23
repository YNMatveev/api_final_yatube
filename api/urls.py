from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentViewSet, FollowCreateListViewSet,
                    GroupCreateListViewSet, PostViewSet)


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet,
                   basename='comment')
router_v1.register(r'group', GroupCreateListViewSet, basename='group')
router_v1.register(r'follow', FollowCreateListViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]
