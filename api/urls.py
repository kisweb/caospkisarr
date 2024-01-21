from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from django.contrib.admin.views.decorators import staff_member_required

from account.models import User
from etablissement.models import Etablissement, Quote
from core.models import Profile, Role
from anneescolaire.models import AnneeScolaire

from .schemas import (
    Error,
    CreateEtablissementSchema,
    UserSchema,
    RoleSchema,
    ProfileSchema,
    AnneeScolaireSchema,
    EtablissementSchema,
    QuoteSchema,
)

app = NinjaAPI(
        docs_decorator=staff_member_required,
        
        openapi_extra={
            "info": { "termsOfService": "https://example.com/terms/", }
            },
        title="CAOSP API",
        description="Les données brutes de CAOSP de Ziguinchor pour la gestion des quoteparts"
    )



@app.get("users/", response=list[UserSchema])
def get_users(request):
    users = User.objects.all()
    return users

@app.get("profiles/", response=list[ProfileSchema])
def get_profiles(request):
    profiles = Profile.objects.all()
    return profiles


@app.get("annees/", response=list[AnneeScolaireSchema])
def get_annees(request):
    annees = AnneeScolaire.objects.all()
    return annees


@app.get("roles/", response=list[RoleSchema])
def get_roles(request):
    roles = Role.objects.all()
    return roles


@app.get("etablissements/", response=list[EtablissementSchema])
def get_etablissements(request):
    etablissements = Etablissement.objects.all()
    return etablissements


@app.get("etablissements/{slug}", response=EtablissementSchema)
def get_etablissements(request, slug):
    etablissement = get_object_or_404(Etablissement, slug=slug)
    return etablissement


@app.post("etablissements/", response={200: EtablissementSchema, 404: Error})
def create_etablissement(request, etablissement: CreateEtablissementSchema):
    etablissement_data = etablissement.model_dump()
    etablissement_model = Etablissement.objects.create(**etablissement_data)
    return etablissement_model


@app.get("quotes/", response=list[QuoteSchema])
def get_quotes(request):
    quotes = Quote.objects.all()
    return quotes
