from django.shortcuts import get_object_or_404,render

# Create your views here.
from .models import Producto
from .models import Categoria
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categories_list = Categoria.objects.all()
    context ={'product_list':product_list,
              'catgories_list':categories_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categories_list = Categoria.objects.all()
    return render(request, 'producto.html', {'producto':producto,'catgories_list':categories_list})

def cat_prod(request, categoria_id):
    categories_list = Categoria.objects.all()
    category = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'productos_cat.html',{'categories_list':categories_list,'categoria':category})