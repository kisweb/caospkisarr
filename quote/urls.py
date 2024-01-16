from django.urls import path
from . import views

app_name = 'quote'


urlpatterns = [ 
    path('', views.QuoteView.as_view(), name='index'),
    path('add-etablissement', views.AddEtablissementView.as_view(), name='add-etablissement'),
    path('add-quote', views.AddQuoteView.as_view(), name='add-quote'),
    path('view-quote/<int:pk>', views.QuoteVisualizationView.as_view(), name='view-quote'),
    path('quote-pdf/<int:pk>', views.get_quote_pdf, name="quote-pdf")
]