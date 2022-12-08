from rest_framework.serializers import ModelSerializer
import

class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        field = ['id', 'title', 'code', 'linenos', 'language', 'style']