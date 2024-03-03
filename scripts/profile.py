from django.db import connection
from pprint import pprint

from core.models import Profile, Role


def run():
    # email = 'cem-ahoune-sane@caosp.zig'
    # mail = email.split('@')[0]
    # # email = mail+'@caosp.zig'
    # print(mail)
    profiles = [
            {
                "id": 8,
                "email": "arfang_bessire_sonko@caosp.zg",
                "name": "CEM ARFANG BESSIRE SONKO",
                "is_active": True
            },
            {
                "id": 10,
                "email": "baila@caosp.zg",
                "name": "CEM BAILA",
                "is_active": True
            },
            {
                "id": 11,
                "email": "brindiago@caosp.zg",
                "name": "CEM BRINDIAGO",
                "is_active": True
            },
            {
                "id": 14,
                "email": "diango@caosp.zg",
                "name": "CEM DIANGO",
                "is_active": True
            },
            {
                "id": 15,
                "email": "djibidione@caosp.zg",
                "name": "CEM DJIBIDIONE",
                "is_active": True
            },
            {
                "id": 16,
                "email": "mampalago@caosp.zg",
                "name": "CEM MAMPALAGO",
                "is_active": True
            },
            {
                "id": 17,
                "email": "ndieba@caosp.zg",
                "name": "CEM NDIEBA",
                "is_active": True
            },
            {
                "id": 18,
                "email": "niamone1@caosp.zg",
                "name": "CEM NIAMONE 1",
                "is_active": True
            },
            {
                "id": 19,
                "email": "niamone2@caosp.zg",
                "name": "CEM NIAMONE 2",
                "is_active": True
            },
            {
                "id": 20,
                "email": "niankitte@caosp.zg",
                "name": "CEM NIANKITTE",
                "is_active": True
            },
            {
                "id": 13,
                "email": "coubanao@caosp.zg",
                "name": "CEM COUBANAO",
                "is_active": True
            },
            {
                "id": 12,
                "email": "coubalan@caosp.zg",
                "name": "CEM COUBALAN",
                "is_active": True
            },
            {
                "id": 7,
                "email": "ahoune_sane@caosp.zg",
                "name": "CEM AHOUNE SANE",
                "is_active": True
            },
            {
                "id": 9,
                "email": "badioure@caosp.zg",
                "name": "CEM BADIOURE",
                "is_active": True
            }
        ]
    
{
    "user": {
      "id": 7,
      "password": "pbkdf2_sha256$720000$dLuxbrZVPpcHi5Jn04Tlr9$7FQTn5wSO/zkza3UwCcQZhqjX260UN52ff+fJPOSfSs=",
      "email": "ahoune_sane@caosp.zg",
      "name": "CEM AHOUNE SANE",
      "is_active": true,
      "is_superuser": false,
      "is_staff": false,
      "date_joined": "2024-01-20T10:03:00",
      "last_login": "2024-01-24T00:23:38.479",
      "groups": [],
      "user_permissions": []
    },
    "role": {
      "id": 3,
      "name": "Utilisateur"
    },
    "id": 3,
    "username": "cemas",
    "bio": "",
    "phone_number": "",
    "birth_date": null
  },
    
    user
    first_name
    last_name
    username
    bio
    phone_number
    birth_date
    role
    item = Profile()
    for profile in profiles:
        item = 
    
    pprint(profiles[0])
    pprint(connection.queries)