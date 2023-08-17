from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("contact_form_submit/", views.contact_form_submit, name="contact_form_submit"),
    path("about_us/", views.about_us, name="about_us"),
    path("profile/", views.profile, name="profile"),
    path(
        "accounts/logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"
    ),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews/create/", views.create_review, name="create_review"),
    path("reviews/delete/<int:review_id>/", views.delete_review, name="delete_review"),
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
