from rest_framework.serializers import ModelSerializer
from .models import Video, Like
from environs import Env

env = Env()
env.read_env()


class AllReelsSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['video'] = f'{env.str("DOMEN")}{instance.video.url}'
        redata['subcategory'] = instance.subcategory.name

        return redata


class RecommendationsSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['video'] = f'{env.str("DOMEN")}{instance.video.url}'
        redata['subcategory'] = instance.subcategory.name

        return redata

