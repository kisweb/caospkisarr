import json 
import os 
from pathlib import Path

from django.conf import settings

def load_fixture(app, fixture_name): 
    """ Load fixture from file and as parsed json, or the text of the file. """
    
    fixture_path = Path(os.path.join(settings.BASE_DIR, app, "core", "fixtures", fixture_name))  

    with open(fixture_path) as f:

        if fixture_path.suffix == ".json":
            fixture = json.load(f)
        else:
            fixture = f.read()
        return fixture