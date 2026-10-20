from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RequestPassworReset, ResetPassword, UserViewSet, ActivateUserView
from posts.views import PostViewSet
from comments.views import CommnentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet)
router.register(r'comments', CommnentViewSet)

urlpatterns = router.urls + [
    path('users/activate/<int:user_id>/', ActivateUserView),
    path('users/reset', RequestPassworReset),
    path('users/reset/<uidb64>/<token>/', ResetPassword),
]
