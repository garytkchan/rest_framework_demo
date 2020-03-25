
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [

    # for routers/viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # Below is funcitoned based
    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail)

    # Class based. because its a class, we  need to add as_view()
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view())
]
