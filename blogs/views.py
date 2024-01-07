from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


from .models import Blog
from .serializers import BlogSerializer


# Create your views here.
class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCreate(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f"'{instance.title}' post has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserPostsList(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        name = user.get_full_name()
        return Blog.objects.filter(author=name)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        username = self.kwargs['username']
        user = User.objects.get(username=username)

        user_data = {
            "id": user.id,
            "author": user.get_full_name(),
            "posts": serializer.data,
        }
        return Response(user_data)




