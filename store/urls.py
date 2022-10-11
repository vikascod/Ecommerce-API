from django.urls import path
from store.views import ListBookView, DetailBookView, ListCategoryView, DetailCategoryView, ListProductView, DetailProductView, ListUser, DetailUser, ListCart, DetailCart


urlpatterns = [
    path('category/', ListCategoryView.as_view(), name='category'),
    path('category/<int:pk>/', DetailCategoryView.as_view(), name='dcategory'),

    path('book/', ListBookView.as_view(), name='book'),
    path('book/<int:pk>/', DetailBookView.as_view(), name='dbook'),

    path('product/', ListProductView.as_view(), name='product'),
    path('product/<int:pk>/', DetailProductView.as_view(), name='dproduct'),    

    path('users/', ListUser.as_view(), name='user'),
    path('users/<int:pk>/', DetailProductView.as_view(), name='duser'),

    path('cart/', ListCart.as_view(), name='cart'),
    path('cart/<int:pk>/', DetailCart.as_view(), name='scart'),
]
