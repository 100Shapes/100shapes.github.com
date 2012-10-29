import hashlib
import requests
import json
from pelican import signals

"""
Gravatar plus plugin for Pelican
================================

This plugin assigns the ``author_gravatar`` variable to the Gravatar URL and
makes the variable available within the article's context.

Settings:
---------

Add AUTHOR_EMAIL to your settings file to define the default author's email
address. Obviously, that email address must be associated with a Gravatar
account.

Article metadata:
------------------

:email:  article's author email

If one of them are defined, the author_gravatar variable is added to the
article's context.
"""

GRAVATARS = {}

def add_gravatar(generator, metadata):

    #first check email
    if 'email' not in metadata.keys()\
        and 'AUTHOR_EMAIL' in generator.settings.keys():
            metadata['email'] = generator.settings['AUTHOR_EMAIL']
    
    #then add gravatar url
    if 'email' in metadata.keys():
        email = metadata['email']
        gravatar = GRAVATARS.get(email, None)
        if not gravatar:
            gravatar_profile_url = "http://en.gravatar.com/" + \
                            hashlib.md5(metadata['email'].lower()).hexdigest() + '.json'
            res = requests.get(gravatar_profile_url)
            # Example response: http://en.gravatar.com/205e460b479e2e5b48aec07710c08d50.json
            if res.status_code == requests.codes.ok:
                gravatar = json.loads(res.text)['entry'][0]
                GRAVATARS.update({email:gravatar})
            else:
                print("Gravatar_plus: no gavitar found");
        
        metadata["author_gravatar"] = gravatar['thumbnailUrl']
        metadata["author_name"] = gravatar['displayName']


def register():
    signals.article_generate_context.connect(add_gravatar)