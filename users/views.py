from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer

def home(request):
    return render(request, 'index.html')

# ViewSets define the view behavior.
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py#L235


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        """
        Set user password

        POST /api/v1/users/:id/set_password/
        """
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        """
        List recent users

        GET /api/v1/users/recent_users/
        """
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
        List a queryset.
        """
        # get and filter queryset
        queryset = self.filter_queryset(self.get_queryset())

        # paginate queryset (optional)
        page = self.paginate_queryset(queryset)
        if page is not None:
            # serialize and send response
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # serialize and send response
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create a model instance.
        """
        # validate request after serialize
        # ...

        # serialize the request data/body
        serializer = self.get_serializer(data=request.data)

        # validate data or return 400 Bad Request
        serializer.is_valid(raise_exception=True)

        # save new instance
        serializer.save()

        # send response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        Retrieve a model instance.
        """
        # get instance
        instance = User.objects.get(pk=pk)
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update a model instance.
        """
        # partial update or full update
        partial = kwargs.pop('partial', False)
        instance = User.objects.get(pk=pk)

        # update current instance with request data
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # save instance
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Destroy a model instance.
        https://github.com/encode/django-rest-framework/blob/19655edbf782aa1fbdd7f8cd56ff9e0b7786ad3c/rest_framework/mixins.py#L85
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
