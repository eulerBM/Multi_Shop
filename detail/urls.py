from detail.views import detail, review
from django.urls import path

urlpatterns = [
    path('<int:id>', detail, name='detail' ),
    path('review/<int:id>', review, name='review_user')
]