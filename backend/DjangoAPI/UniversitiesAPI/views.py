from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UniversitiesAPI.models import Country, Region, City, University
from UniversitiesAPI.serializers import CountrySerializer, RegionSerializer, CitySerializer, UniversitySerializer

from django.core.files.storage import default_storage
from django.conf import settings


# Create your views here.


@csrf_exempt
def countriesApi(request, id=1):
    if request.method == 'GET':
        countries = Country.objects.all()
        countries_serializer = CountrySerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)

    elif request.method == 'POST':
        country_data = JSONParser().parse(request)
        countries_serializer = CountrySerializer(data=country_data)

        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(f"Country '{country_data['CountryName']}' added successfully.", safe=False)
        return JsonResponse("Failed to add country.", safe=False)


@csrf_exempt
def regionsApi(request, id=1):
    if request.method == 'GET':
        regions = Region.objects.all()
        regions_serializer = RegionSerializer(regions, many=True)
        return JsonResponse(regions_serializer.data, safe=False)

    elif request.method == 'POST':
        regions_data = JSONParser().parse(request)
        regions_serializer = RegionSerializer(data=regions_data)

        if regions_serializer.is_valid():
            regions_serializer.save()
            return JsonResponse(f"Region '{regions_data['RegionName']}' added successfully.", safe=False)
        return JsonResponse("Failed to add region.", safe=False)


@csrf_exempt
def citiesApi(request, id=2):
    if request.method == 'GET':
        cities = City.objects.all()
        cities_serializer = CitySerializer(cities, many=True)
        return JsonResponse(cities_serializer.data, safe=False)

    elif request.method == 'POST':
        cities_data = JSONParser().parse(request)
        cities_serializer = CitySerializer(data=cities_data)

        if cities_serializer.is_valid():
            cities_serializer.save()
            return JsonResponse(f"City '{cities_data['CityName']}' added successfully.", safe=False)
        return JsonResponse("Failed to add city.", safe=False)


@csrf_exempt
def universitiesApi(request, id=3):
    if request.method == 'GET':
        universities = University.objects.all()
        universities_serializer = UniversitySerializer(universities, many=True)
        return JsonResponse(universities_serializer.data, safe=False)

    elif request.method == 'POST':
        university_data = JSONParser().parse(request)
        universities_serializer = UniversitySerializer(data=university_data)
        if universities_serializer.is_valid():
            universities_serializer.save()
            return JsonResponse(f"University {university_data['UniversityName']} added successfully.", safe=False)
        return JsonResponse("Failed to add university.", safe=False)
