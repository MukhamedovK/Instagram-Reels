from rest_framework.serializers import ModelSerializer
from .models import Video, Like


class AllReelsSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['video'] = instance.video.url
        redata['subcategory'] = instance.subcategory.name

        return redata


class RecommendationsSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['subcategory'] = instance.subcategory.name

        return redata

