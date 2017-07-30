
# -*- coding: utf-8 -*-
# -----------------------------------------Import a file for another files----------------------------------------------------------
from __future__ import unicode_literals

from django.db import models
import uuid
#----------------------------------------- Create your models here-----------------------------------------------------------------------.
class UserModel(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=255)
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add = True)
    Updated_on = models.DateTimeField(auto_now=True)


#----------------------------------------- Create a session model here---------------------------------------------------------------
class SessionToken(models.Model):
        user = models.ForeignKey(UserModel)
        session_token = models.CharField(max_length=255)
        last_request_on = models.DateTimeField(auto_now=True)
        created_on = models.DateTimeField(auto_now_add=True)
        is_valid = models.BooleanField(default=True)

        def create_token(self):
            self.session_token = uuid.uuid4()

#--------------------------------------------Create a postmodel of user---------------------------------------------------------------
class PostModel(models.Model):
	    user = models.ForeignKey(UserModel)
	    image = models.FileField(upload_to='user_images')
	    image_url = models.CharField(max_length=255)
	    caption = models.CharField(max_length=240)
	    created_on = models.DateTimeField(auto_now_add=True)
	    updated_on = models.DateTimeField(auto_now=True)
	    has_liked = False


	    @property
	    def like_count(self):
		return len(LikeModel.objects.filter(post=self))

	    @property
	    def comments(self):
		return CommentModel.objects.filter(post=self).order_by('created_on')


#------------------------------------------- Create a like model of user-------------------------------------------------------------
class LikeModel(models.Model):
	    user = models.ForeignKey(UserModel)
	    post = models.ForeignKey(PostModel)
	    created_on = models.DateTimeField(auto_now_add=True)
	    updated_on = models.DateTimeField(auto_now=True)


# --------------------------------------------Create a Comment model for user-------------------------------------------------------------------
class CommentModel(models.Model):
	    user = models.ForeignKey(UserModel)
	    post = models.ForeignKey(PostModel)
	    comment_text = models.CharField(max_length=555)
	    created_on = models.DateTimeField(auto_now_add=True)
	    updated_on = models.DateTimeField(auto_now=True)