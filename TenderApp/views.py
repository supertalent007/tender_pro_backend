from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import ExeTeamMember, Home, Testimonial, Product, Benefit, Team, Advisor, DesignPrivacy, OurValue, New, HomeProcessHeader, HomeProcessContent
from rest_framework.decorators import api_view

# Create your views here.

def my_api_test(request):
    param1_value = request.GET.get('param1')
    param2_value = request.GET.get('param2')
    data = {
        'message': 'Hello, world!',
        'method': request.method,
        'path': request.path,
        'user_agent': request.headers.get('User-Agent'),
        'param1': param1_value,
        'param2': param2_value
        }
    return JsonResponse(data)

def getExeTeamMembers(request):
    teamData = ExeTeamMember.objects.all().values()
    resData = {
        'teamMembers': list(teamData),
    }
    return JsonResponse(resData)

@api_view(['GET'])

def get_home_page_header(request):
    home_object = Home.objects.all().first()
    fields = ['title', 'description', 'image', 'analysis_title', 'households', 'data_sources', 'attr_per_record', 'market_listing_coverage', 'data_points', 'address_match_accuracy', 'compliant']
    
    values = {
        field: getattr(home_object, field).url if field == 'image' and getattr(home_object, field) else getattr(home_object, field)
        for field in fields
    }

    return Response(values)

@api_view(['GET'])

def get_home_process_header(request):
    home_object = HomeProcessHeader.objects.all().first()
    fields = ['title', 'sub_title', 'image']
    
    values = {
        field: getattr(home_object, field).url if field == 'image' and getattr(home_object, field) else getattr(home_object, field)
        for field in fields
    }

    return Response(values)

@api_view(['GET'])

def get_home_process_content(request):
    objects = HomeProcessContent.objects.all()
    fields = ['id', 'title', 'content']
    result = []

    for object in objects:
        values = {field: getattr(object, field) for field in fields}
        result.append(values)
    
    return Response(result)

@api_view(['GET'])

def get_testimonials(request):
    testimonials = Testimonial.objects.all()

    testimonials_with_user_info = []
    
    # Iterate over each testimonial
    for testimonial in testimonials:
        try:
            # Attempt to find the corresponding ExeTeamMember by user_id
            team_member = ExeTeamMember.objects.get(id=testimonial.user_id)
        except ExeTeamMember.DoesNotExist:
            # If no matching ExeTeamMember is found, skip this testimonial
            continue
        
        # Extract relevant fields from the team_member
        user_info = {
            "first_name": team_member.first_name,
            "last_name": team_member.last_name,
            "role": team_member.role,
            "avatar": team_member.avatar.url if team_member.avatar else None,
        }
        
        # Combine user info with testimonial content into a single dictionary
        testimonial_data = {
            "content": testimonial.content,
            "company": testimonial.company.url if testimonial.company else None,  # Assuming social field contains company information
            **user_info
        }
        
        # Append the combined data to our list
        testimonials_with_user_info.append(testimonial_data)
    
    # Return the data as a JSON response
    return Response(testimonials_with_user_info)

@api_view(['GET'])

def get_products(request):
    products = Product.objects.all()
    fields = ['id', 'name', 'description']
    product_list = []

    for product in products:
        values = {field: getattr(product, field) for field in fields}
        product_list.append(values)
    
    return Response(product_list)

@api_view(['GET'])

def get_single_product(request, id):
    product = Product.objects.get(id=id)
    fields = ['id', 'name', 'description', 'image', 'product_section_title', 'product_section_content', 'product_description_title', 'product_description_content']
    values = {
        field: getattr(product, field).url if field == 'image' and getattr(product, field) else getattr(product, field)
        for field in fields
    }
    
    return Response(values)

@api_view(['GET'])

def get_product_benefits(request, id):
    benefits = Benefit.objects.filter(product_id = id)
    fields = ['id', 'title', 'content']
    res_benefits = []

    for benefit in benefits:
        values = {field: getattr(benefit, field) for field in fields}
        res_benefits.append(values)
    
    return Response(res_benefits)

@api_view(['GET'])

def get_team(request):
    team = Team.objects.all()
    team_members = []

    for team_member in team:
        data = {
            "id": team_member.id,
            "first_name": team_member.first_name,
            "last_name": team_member.last_name,
            "role": team_member.role,
            "social": team_member.social,
            "avatar": team_member.avatar.url if team_member.avatar else None,
        }
        team_members.append(data)
    
    return Response(team_members)

@api_view(['GET'])

def get_advisor(request):
    advisors = Advisor.objects.all()
    advisor_members = []

    for advisor in advisors:
        data = {
            "id": advisor.id,
            "first_name": advisor.first_name,
            "last_name": advisor.last_name,
            "role": advisor.role,
            "avatar": advisor.avatar.url if advisor.avatar else None,
        }
        advisor_members.append(data)
    
    return Response(advisor_members)

@api_view(['GET'])

def get_design_privacy(request):
    designPrivacies = DesignPrivacy.objects.all()
    fields = ['id', 'title', 'content']
    res = []

    for privacy in designPrivacies:
        values = {field: getattr(privacy, field) for field in fields}
        res.append(values)
    
    return Response(res)


@api_view(['GET'])

def get_our_values(request):
    values = OurValue.objects.all()
    fields = ['id', 'title', 'content', 'image']
    res = []

    for val in values:
        values = {field: getattr(val, field) for field in fields}
        res.append(values)
    
    return Response(res)

@api_view(['GET'])

def get_news(request):
    values = New.objects.all()
    res = []

    for val in values:
        data = {
            "id": val.id,
            "image": val.image.url if val.image else None,
        }

        res.append(data)
    
    return Response(res)