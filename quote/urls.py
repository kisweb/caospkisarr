from django.urls import path
from . import views

app_name = 'quote'


urlpatterns = [ 
    path('', views.QuoteView.as_view(), name='index'),
    # path('add-etablissement', views.AddEtablissementView.as_view(), name='add-etablissement'),
    # path('add-quote', views.AddQuoteView.as_view(), name='add-quote'),
    path('view-quote/', views.voir_quotes, name='view-quotes'),
    path('quote-pdf/', views.getPDF, name="quote-pdf"),
    path('pdf/', views.get_quote_pdf, name="pdf")
]