from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Video, Like
from .serializers import AllReelsSerializer, RecommendationsSerializer
from .utils import like_status


def home_page(request):
    return render(request, "instagram/home.html")


class Permissions(APIView):
    permission_classes = [IsAuthenticated]


class AllReelsView(Permissions):

    def get(self, request):
        all_videos = Video.objects.all()
        serializer = AllReelsSerializer(instance=all_videos, many=True)
        
        videos = like_status(serializer=serializer, user=request.user)

        return Response(videos.data, status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        video_id = int(request.data.get('id'))
        user = request.user

        video = Video.objects.get(id=video_id)
        user_like = Like.objects.filter(user=user, liked_video=video)

        serializer = AllReelsSerializer(instance=video)
        if not user_like.exists():
            Like.objects.create(user=user, liked_video=video)
        else:
            user_like.delete()
            return Response("Like removed!", status=status.HTTP_200_OK)
        video.save()

        return Response({"Liked!": serializer.data}, status=status.HTTP_201_CREATED)


class RecommendationsView(Permissions):

    def get(self, request):
        likes_count = Video.objects.all().order_by('-create_at', '-video_likes')
        serializer = RecommendationsSerializer(instance=likes_count, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    
