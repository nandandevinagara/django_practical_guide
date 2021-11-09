from django.urls import path
from . import views

urlpatterns = [
    # int should be first because if str is first, then 1 is considered as string and executed
    path("", views.index, name="challenges_home"),
    path("<int:month>/", views.monthly_challenge_num),
    path("<str:month>/", views.monthly_challenge, name="month_str_url"),
]
