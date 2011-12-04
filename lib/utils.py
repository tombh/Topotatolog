from blog.models import UserProfile
from django.template.defaultfilters import slugify

import sys
from pprint import pprint

def socregUserCreate(user, profile, api):
    
    #Facebook API call
    info = api.graph.request(profile.uid, {'fields' : 'picture, username, first_name, last_name'})    
    
    #pprint("1")
    #pprint(info)
    #pprint(vars(profile))    
    #pprint("2")
    #sys.exit()
    
    if info['username']:
        user.username = info['username']
    else:
        user.username = slugify(info['first_name'] + info['lastname'])
    user.email = 'dummy@email.com'
    user.save()
    up = UserProfile(avatar=info['picture'], user=user)
    up.save()
    
    return user.username