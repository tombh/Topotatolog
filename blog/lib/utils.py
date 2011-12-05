from blog.models import UserProfile
from django.template.defaultfilters import slugify

import sys
from pprint import pprint

def socregUserCreate(user, profile, api):
    """
    This is the callback after a user has succuessfully connected their social network.
    I'm mainly using it here to add the user's profile picture.
    """
    
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
    
    # Providing a dummy email allows us to automatically post comments,
    # by hiding all fields apart from the comment body
    user.email = 'dummy@email.com'
    
    # The user doesn't actually exist in the DB yet.
    # Without persisting it UserProfile throws a wobbly :( 
    user.save()
    
    # Add the avatar
    up = UserProfile(avatar=info['picture'], user=user)
    up.save()
    
    # Return the username out of courtesy, it's not actually required
    return user.username