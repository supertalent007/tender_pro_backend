from django.contrib import admin
from .models import ExeTeamMember, Home, Testimonial, Product, Benefit, Team, Advisor, DesignPrivacy, OurValue, New, HomeProcessHeader, HomeProcessContent
# Register your models here.
class ExeTeamMemberAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "role", "description", "avatar")

admin.site.register(ExeTeamMember, ExeTeamMemberAdmin)

class HomeAdmin(admin.ModelAdmin):
  list_display = ("id", "title", "description", "image", "analysis_title", "households", "data_sources", "attr_per_record", "market_listing_coverage", "data_points", "address_match_accuracy", "compliant")
  search_fields = ("id", "title", "description", "image", "analysis_title", "households", "data_sources", "attr_per_record", "market_listing_coverage", "data_points", "address_match_accuracy", "compliant")
  list_filter = ("id", "title", "description", "image", "analysis_title", "households", "data_sources", "attr_per_record", "market_listing_coverage", "data_points", "address_match_accuracy", "compliant")

admin.site.register(Home, HomeAdmin)

class HomeProcessHeaderAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'sub_title', 'image')
  search_fields = ('id', 'title', 'sub_title', 'image')
  list_filter = ('id', 'title', 'sub_title', 'image')

admin.site.register(HomeProcessHeader, HomeProcessHeaderAdmin)

class HomeProcessContentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'content')
  search_fields = ('id', 'title', 'content')
  list_filter = ('id', 'title', 'content')

admin.site.register(HomeProcessContent, HomeProcessContentAdmin)

class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('user_id', 'content', 'company')
  search_fields = ('user_id', 'content', 'company')
  list_filter = ('user_id', 'content', 'company')

admin.site.register(Testimonial, TestimonialAdmin )

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'image', 'product_section_title', 'product_section_content', 'product_description_title', 'product_description_content')

admin.site.register(Product, ProductAdmin )

class BenefitAdmin(admin.ModelAdmin):
  list_display = ('product_id', 'title', 'content')

admin.site.register( Benefit, BenefitAdmin )


class TeamAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'role', 'avatar', 'social')

admin.site.register( Team, TeamAdmin )


class AdvisorAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'role', 'avatar')

admin.site.register( Advisor, AdvisorAdmin )


class DesignPrivacyAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'content')

admin.site.register( DesignPrivacy, DesignPrivacyAdmin )

class OurValuesAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'content', 'image')

admin.site.register( OurValue, OurValuesAdmin )

class NewsAdmin(admin.ModelAdmin):
  list_display = ('id', 'image')

admin.site.register( New, NewsAdmin )