import datetime
from ninja import ModelSchema, Schema

from account.models import User
from etablissement.models import Etablissement, Quote
from core.models import Profile, Role
from anneescolaire.models import AnneeScolaire


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = "__all__"


class RoleSchema(ModelSchema):
    class Meta:
        model = Role
        fields = (
            "id",
            "name",
        )


class AnneeScolaireSchema(ModelSchema):
    class Meta:
        model = AnneeScolaire
        fields = (
            "id",
            "annee",
            "active",
            "statut",
        )


class ProfileSchema(ModelSchema):
    user: UserSchema
    role: RoleSchema | None = None

    class Meta:
        model = Profile
        fields = ("id", "user","username", "bio", "phone_number", "birth_date", "role")


class EtablissementSchema(ModelSchema):
    class Meta:
        model = Etablissement
        fields = "__all__"


class CreateEtablissementSchema(Schema):
    name: str
    ief_id: int
    type_etablissement: str
    nomce: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    save_by_id: int | None = None


class Error(Schema):
    message: str


class QuoteSchema(ModelSchema):
    class Meta:
        model = Quote
        fields = "__all__"
