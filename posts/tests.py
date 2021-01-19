from django.test import TestCase
from .models import Post
from users.models import User

class PostTest(TestCase):

    def test_for_Django_ORM(self):

        user = User.objects.create(username='admin', email='rnovelo.cruz98@gmail.com')
        user.save()

        # creating instances
        instance = Post.objects.create(title='Sunny Day at Las Vegas', user=user)
        instance.save()
        
        # get all table instances
        queryset = Post.objects.all()
        print(queryset) # always return a QuerySet


        # filtering instances
        queryset = Post.objects.filter(title__icontains='Trump')
        # queryset = Post.objects.filter(created_at__range=['2020-01-01', '2020-01-02'])
        # queryset = Post.objects.filter(created_at='2020-01-01')
        queryset = Post.objects.filter(user_id__lte=1)
        queryset = Post.objects.filter(user_id__gte=1, title="Pepe")
        print(queryset) # always return a QuerySet

        try:
            instance = Post.objects.get(pk=1)
            print(instance) # always return a Post instance


            # update and instance
            instance.title = 'Test'
            instance.save()

        except Post.DoesNotExist:
            print('DoesNotExist called')

        
        
