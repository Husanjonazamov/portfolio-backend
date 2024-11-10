from rest_framework import serializers
from portfolio.models import Category, Portfolio





class PortfolioSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'desc', 'category', 'image', 'githup', 'projects']
        
    def get_category(self, obj):
        return obj.category.name if obj.category else None



class CategorySerializer(serializers.ModelSerializer):
    portfolios = PortfolioSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'portfolios']
        
        
        