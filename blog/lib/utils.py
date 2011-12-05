from blog.models import UserProfile
from django.template.defaultfilters import slugify
import json

def socregUserCreate(user, profile, api):
    """
    This is the callback from the socialregistration app after a user has succuessfully connected their social network.
    I'm mainly using it here to add the user's profile picture.
    """
    
    info = {}
    
    # --------------------
    # Twitter API call
    # --------------------
    if hasattr(profile, 'twitter_id'):
        response = api.request("https://api.twitter.com/users/" + profile.twitter_id + ".json")
        
        #response is only a JSON string at the moment 
        details = json.loads(response)  
        
        info['picture'] = details['profile_image_url']
        info['username'] = details['screen_name']
           
    # --------------------
    # Facebook API call
    # --------------------
    else:
        info = api.graph.request(profile.uid, {'fields' : 'picture, username, first_name, last_name'})
    
    
    # Create the username for Django's User model
    if info['username']:
        user.username = info['username']
    else:
        #If there's no username slugify one from their real name
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