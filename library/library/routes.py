from rest_framework import routers
from books.views import BookViewSet, AuthorViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='authors')
urlpatterns = router.urls