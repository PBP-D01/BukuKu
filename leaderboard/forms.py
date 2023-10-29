from django.forms import ModelForm
from leaderboard.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
