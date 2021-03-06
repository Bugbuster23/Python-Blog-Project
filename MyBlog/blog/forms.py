from django.forms import ModelForm, Textarea, TextInput
from blog.models import Post,Comment

#CREATE FORMS here
class PostForm(ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':TextInput(attrs={'class':'textinputclass',}),
            'text':Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':TextInput(attrs={'class':'textinputclass'}),
            'text':Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }
