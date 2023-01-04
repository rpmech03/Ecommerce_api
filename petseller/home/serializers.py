from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = '__all__'

class AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalColor
        fields = '__all__'

class AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImages
        fields = ['animal_images']


class AnimalSerializer(serializers.ModelSerializer):
    animal_category = serializers.SerializerMethodField()
    animal_color = AnimalColorSerializer(many = True)
    animal_breed = AnimalBreedSerializer(many = True)
    # images = AnimalImagesSerializer(many = True)

    def get_animal_category(self, obj):
        return obj.animal_category.category_name

    def create(self, data):
        animal_breed = data.pop('animal_breed')
        animal_color = data.pop('animal_color')

        animal = Animal.objects.create(**data, animal_category = Category.objects.get(category_name="Dog"))

        for ab in animal_breed:
            # print(ab['animal_breed'])
            animal_breed_obj = AnimalBreed.objects.get(animal_breed=ab['animal_breed'])
            animal.animal_breed.add(animal_breed_obj)

        for ac in animal_color:
            # print(ac['animal_breed'])
            animal_color_obj = AnimalColor.objects.get(animal_color=ac['animal_color'])
            animal.animal_breed.add(animal_color_obj)


        return Animal.objects.first()

        # return animal
        # print(data)

 
    class Meta:
        model = Animal
        # fields = '__all__'
        exclude = ['updated_at']

class AnimalLocation(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocation
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username = data['username'])
            if user.exists():
                raise serializers.ValidationError('username is already taken')

        if 'email' in data:
            user = User.objects.filter(email = data['email'])
            if user.exists():
                raise serializers.ValidationError('email is already taken')
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username = data['username'])
            if not user.exists():
                raise serializers.ValidationError('username does not exist')
        return data
