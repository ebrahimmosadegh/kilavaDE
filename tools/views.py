import os
from django.shortcuts import render
from django.core.exceptions import ValidationError
import random
import string
from django.utils.text import slugify


# Create your views here.
def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.bmp', '.gif', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('This file not suported, please try edit')

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mpg', '.avi', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('This file not suported, please try edit')



'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print(random_string_generator())

print(random_string_generator(size=50))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
