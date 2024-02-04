from django.urls import path
from . import views
urlpatterns = [
    path('csv_visualization/',views.csvfile_visualization,name = 'csv_visualization'),
    path('csv_question/',views.visualization_question,name = 'csv_question'),
    path('upload_file/',views.upload_file,name = 'upload_file'),
]