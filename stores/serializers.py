from rest_framework import serializers
from models import Store, Item

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'description')
    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    # items = serializers.HyperlinkedRelatedField(many=True, read_only=True,
    #                                              view_name='item-detail')
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Store` instance, given the validated data.
    #     """
    #     return Store.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance

class ItemSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    desription = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    expired = serializers.BooleanField(required=True)
    expiration = serializers.DateTimeField(required=False)
    store = serializers.HyperlinkedRelatedField(many=False, read_only=True,
                                                 view_name='store')
    def create(self, validated_data):
        """
        Create and return a new `Store` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.expired = validated_data.get('expired', instance.expired)
        instance.expiration = validated_data.get('expiration', instance.expiration)
        instance.save()
        return instance