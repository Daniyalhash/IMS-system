from django.urls import path


from .views import *
urlpatterns = [
    path('',index,name='home'),

   #  dashboard
    path('dashboard/',dashboard,name='dashboard'),
    # product path
   path('product/',product,name='product'),
   path('save_product',save_product,name='save_product'),
   path('delete_product/<str:pro_id>',delete_product,name='delete_product'),
   path('update_product/<str:pro_id>/',update_product,name='update_product'),
   path('getproduct',getproduct,name='getproduct'),
   path('editproduct',editproduct,name='editproduct'),
   path('get_length',get_length,name='get_length'),

    #    supplier path
   path('supplier/',supplier,name='supplier'),
   path('save_supplier',save_supplier,name='save_supplier'),
   path('delete_supplier/<str:sup_id>',delete_supplier,name='delete_supplier'),
   path('update_supplier/<str:sup_id>/',update_supplier,name='update_supplier'),
   path('editsupplier',editsupplier,name='editsupplier'),
   # purchase update_supplier
   path('purchase/',purchase,name='purchase'),
      path('save_purchase',save_purchase,name='save_purchase'),
      path('delete_purchase/<str:pur_id>',delete_purchase,name='delete_purchase'),
      path('add-to-cart/', add_to_cart, name='add_to_cart'),
   path('update_purchase/<str:pur_id>/',update_purchase,name='update_purchase'),
   path('editpurchase',editpurchase,name='editpurchase'),

   
   # customer
   path('customer/',customer,name='customer'),
      path('save_customer',save_customer,name='save_customer'),
      path('delete_customer/<str:cus_id>',delete_customer,name='delete_customer'),
   # sales
   path('sale/',sale,name='sale'),
      path('save_sale',save_sale,name='save_sale'),
      path('delete_sale/<str:sal_id>',delete_sale,name='delete_sale'),
      path('add-product-to-cart/', add_to_cart_sale, name='add_to_cart_sale'),
      path('update_sale/<str:sal_id>/',update_sale,name='update_sale'),
   path('editsale',editsale,name='editsale'),
   # inventory
   path('inventory/',display_inventory,name='inventory'),
   path('delete_inventory/<str:in_id>',delete_inventory,name='delete_inventory'),
]
