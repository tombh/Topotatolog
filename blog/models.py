from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
  
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)    

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.CharField(max_length=300)
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])