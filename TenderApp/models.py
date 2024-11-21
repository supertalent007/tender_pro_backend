import os
import random
import string
import uuid

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

def image_custom_path(instance, image_name):
  ext = image_name.split(".")[-1]  # Get the extension of the image
  random_string = "".join(
      random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
      for _ in range(33)
  )
  # Replace the image name with random string
  image_name = "%s.%s" % (random_string, ext)

  return os.path.join("custom/", image_name)

def image_name_and_path(instance, image_name):
  ext = image_name.split(".")[-1]  # Get the extension of the image
  random_string = "".join(
      random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
      for _ in range(33)
  )
  # Replace the image name with random string
  image_name = "%s.%s" % (random_string, ext)

  return os.path.join("accounts/", image_name)

def image_team_path(instance, image_name):
  ext = image_name.split(".")[-1]  # Get the extension of the image
  random_string = "".join(
      random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
      for _ in range(33)
  )
  # Replace the image name with random string
  image_name = "%s.%s" % (random_string, ext)

  return os.path.join("team/", image_name)

def image_advisor_path(instance, image_name):
  ext = image_name.split(".")[-1]  # Get the extension of the image
  random_string = "".join(
      random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
      for _ in range(33)
  )
  # Replace the image name with random string
  image_name = "%s.%s" % (random_string, ext)

  return os.path.join("advisor/", image_name)

def image_news_path(instance, image_name):
  ext = image_name.split(".")[-1]  # Get the extension of the image
  random_string = "".join(
      random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
      for _ in range(33)
  )
  # Replace the image name with random string
  image_name = "%s.%s" % (random_string, ext)

  return os.path.join("advisor/", image_name)

def image_svg_path(instance, filename):
    # Define file path here.
    return 'svg/{}'.format(filename)


class ExeTeamMember(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  role = models.CharField(max_length=255)
  description = models.CharField(max_length=3000)
  social = models.CharField(max_length=3000, default='')
  avatar = models.ImageField(upload_to=image_name_and_path, blank=True, null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}" 

class Home(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam accumsan felis nec')
  image = models.ImageField(upload_to=image_custom_path, blank=True, null=True, default='')
  analysis_title = models.CharField(max_length=255, default='Use our data, science and AI to..')
  households = models.CharField(max_length=255, default='30.8m')
  data_sources = models.CharField(max_length=255, default='60+')
  attr_per_record = models.CharField(max_length=255, default='2300+')
  market_listing_coverage = models.CharField(max_length=255, default='81%')
  data_points = models.CharField(max_length=255, default='75b')
  address_match_accuracy = models.CharField(max_length=255, default='90%')
  compliant = models.CharField(max_length=255, default='GDPR')

  def __str__(self):
    return f"{self.title} {self.description}"
  
class HomeProcessHeader(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to=image_custom_path, blank=True, null=True, default='')
  sub_title = models.CharField(max_length=255)

class HomeProcessContent(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)

class Testimonial(models.Model):
  user_id = models.CharField(max_length=255)
  content = models.CharField( max_length=3000 )
  company = models.ImageField(upload_to=image_name_and_path, blank=True, null=True, default='')

class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=3000)
  image = models.ImageField(upload_to=image_custom_path, blank=True, null=True, default='')
  product_section_title = models.CharField(max_length=255, default='')
  product_section_content = models.CharField(max_length=3000, default='')
  product_description_title = models.CharField(max_length=3000, default='')
  product_description_content = models.CharField(max_length=3000, default='')

class Benefit(models.Model):
  product_id = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=3000)

class Team(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  role = models.CharField(max_length=255)
  social = models.CharField(max_length=255)
  avatar = models.ImageField(upload_to=image_team_path, blank=True, null=True)

class Advisor(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  role = models.CharField(max_length=255)
  avatar = models.ImageField(upload_to=image_advisor_path, blank=True, null=True)

class DesignPrivacy(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=3000)

class OurValue(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=3000)
  image = models.FileField(
      upload_to=image_svg_path,
      validators=[FileExtensionValidator(allowed_extensions=['svg'])],
      blank=True,
      null=True
  )

class New(models.Model):
  image = models.ImageField(upload_to=image_news_path, blank=True, null=True)