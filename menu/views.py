from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Products

# Create your views here.

class MenuView(LoginRequiredMixin,TemplateView):
    pass

dashboard_view = MenuView.as_view(template_name = "menu/index.html") 

# product
product_list_view = MenuView.as_view(template_name = "menu/products/product-list.html") 
product_grid_view = MenuView.as_view(template_name = "menu/products/product-grid.html") 
product_overview_view = MenuView.as_view(template_name = "menu/products/product-overview.html") 
product_create_view = MenuView.as_view(template_name = "menu/products/product-create.html") 
categories_view = MenuView.as_view(template_name = "menu/products/categories.html") 
sub_categories_view = MenuView.as_view(template_name = "menu/products/sub-categories.html") 

# orders
orders_list_view = MenuView.as_view(template_name = "menu/orders/orders-list-view.html") 
orders_overview_view = MenuView.as_view(template_name = "menu/orders/orders-overview.html") 

calendar_view = MenuView.as_view(template_name = "menu/calendar.html") 

# sellers
seller_list_view = MenuView.as_view(template_name = "menu/sellers/sellers-list-view.html") 
seller_grid_view = MenuView.as_view(template_name = "menu/sellers/sellers-grid-view.html") 
seller_overview_view = MenuView.as_view(template_name = "menu/sellers/seller-overview.html") 

# invoice
invoice_list_view = MenuView.as_view(template_name = "menu/invoice/invoices-list.html") 
invoice_details_view = MenuView.as_view(template_name = "menu/invoice/invoices-details.html") 
invoice_create_view = MenuView.as_view(template_name = "menu/invoice/invoices-create.html") 

users_list_view = MenuView.as_view(template_name = "menu/users-list.html") 

# shipping
shipping_list_view = MenuView.as_view(template_name = "menu/shipping/shipping-list.html") 
shipments_view = MenuView.as_view(template_name = "menu/shipping/shipments.html") 

coupons_view = MenuView.as_view(template_name = "menu/coupons.html") 

reviews_rating_view = MenuView.as_view(template_name = "menu/reviews-ratings.html") 

brands_view = MenuView.as_view(template_name = "menu/brands.html") 

statistics_view = MenuView.as_view(template_name = "menu/statistics.html") 

transactions_view = MenuView.as_view(template_name = "menu/localization/transactions.html") 

currency_rates_view = MenuView.as_view(template_name = "menu/localization/currency-rates.html") 
@csrf_exempt  # Temporary disable CSRF for simplicity (consider using csrf protection in production)
def save_data_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # Save data to your model
        your_model_instance = Products(
            # Map your fields from the data object
            id=data.get('id'),
            productImg=data.get('productImg'),
            productTitle=data.get('productTitle'),
            category=data.get('category'),
            price=data.get('price'),
            discount=data.get('discount'),
            rating=data.get('rating'),
            color=data.get('color'),
            size=data.get('size'),
            stock=data.get('stock'),
            orders=data.get('orders'),
            publish=data.get('publish'),
        )
        your_model_instance.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})