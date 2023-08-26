import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(field_name='date_ordered', lookup_expr='gte', label="Start date")
    end_date = django_filters.DateFilter(field_name='date_ordered', lookup_expr='lte', label="End date")
    note = django_filters.CharFilter(field_name='note', lookup_expr='icontains', label='Note')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_ordered']

