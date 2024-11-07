from rest_framework import serializers
from portfolio.models import Category, Portfolio





class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'desc', 'image', 'githup', 'projects']


class CategorySerializer(serializers.ModelSerializer):
    portfolios = PortfolioSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'portfolios']