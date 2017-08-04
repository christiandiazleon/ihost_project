from rest_framework import serializers
from .models import LodgingOffer, StudiesOffert


class LodgingOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgingOffer
        fields = ('url', 'created_by', 'ad_title', 'country', 'city',
            'address', 'lodging_offer_type', 'stars', 'available_dates',
            'offered_services', 'featured_amenities', 'room_type_offered',
             'number_guest_room_type', 'bed_type', 'bathroom',
             'room_information', 'photographies', 'room_value',
             'additional_description' )


class StudiesOffertSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudiesOffert
        fields = ('url', 'created_by', 'ad_title', 'country', 'city',
            'address', 'institute_character',
            'students_number', 'studies_type_offered',
            'academic_mobility_programs', 'duration', 'studies_value',
            'additional_description' )
