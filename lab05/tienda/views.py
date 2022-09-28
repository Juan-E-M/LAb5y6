from django.shortcuts import get_object_or_404,render

# Create your views here.
from .models import Producto

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    context ={'product_list':product_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto':producto})