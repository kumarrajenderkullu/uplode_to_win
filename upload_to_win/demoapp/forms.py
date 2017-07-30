#---------------------------------------Import a file from another files------------------------------------------------------------
from django import forms
from models import UserModel,PostModel,LikeModel, CommentModel

#---------------------------------------Create a class for sifnup form---------------------------------------------------------------
class SignUpForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Email','Username','Name','Password']
#----------------------------------------Create a login form--------------------------------------------------------------------------
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Username','Password']
#-----------------------------------------Create a post form----------------------------------------------------------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']

#-------------------------------------------Craete a likeform---------------------------------------------------------------------------------
class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']

#--------------------------------------------Create a commennt form------------------------------------------------------------------------------
class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']
#--------------------------------------------------End of file--------------------------------------------------------------------------