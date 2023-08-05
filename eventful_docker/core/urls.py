from django.urls import path

from eventful_docker.core.views import newsletter_view


app_name = "core"
urlpatterns = [
    path("<int:id>/", view=newsletter_view, name="newsletter_view"),
]
