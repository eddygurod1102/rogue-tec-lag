from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from .models import Categoria, Subcategoria, Producto
from .forms import FormularioComentario

# Vista para la página de inicio. Mostrará las categorías disponibles de los
# productos.
class VistaListaCategorias(ListView):
    model = Categoria
    template_name = 'inicio.html'
    queryset = Categoria.objects.order_by('nombre')

# Vista que muestra las subcategorías de una categoría.
class VistaListaSubcategorias(ListView):
    model = Subcategoria
    template_name = 'gimnasio/lista/lista_subcategorias.html'

    # Ampliar el contenido del context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la categoría por su llave primaria.
        categoria = Categoria.objects.get(pk = self.kwargs['pk'])

        # Agrego la categoría al context.
        context['categoria'] = categoria

        # Buscar todas las subcategorías de una categoría dada. Agregarla al context.
        context['subcategorias'] = Subcategoria.objects.filter(categoria = categoria).order_by('nombre')
        return context

# Vista que muestra los productos de una subcategoria.
class VistaListaProductos(ListView):
    model = Producto
    template_name = 'gimnasio/lista/lista_productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = Categoria.objects.get(pk = self.kwargs['pk1'])
        subcategoria = Subcategoria.objects.get(pk = self.kwargs['pk2'])
        productos = Producto.objects.filter(categoria = subcategoria).order_by('nombre')
        context['categoria'] = categoria
        context['subcategoria'] = subcategoria
        context['productos'] = productos
        return context
    
# Vista que muestra la información de un solo producto.
class VistaObtenerComentario(DetailView):
    model = Producto
    template_name = 'gimnasio/detalle/detalle_producto.html'
    pk_url_kwarg = 'pk3'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioComentario
        return context

class VistaDetalleProducto(View):
    def get(self, request, *args, **kwargs):
        view = VistaObtenerComentario.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = VistaPublicarComentario.as_view()
        return view(request, *args, **kwargs)

# Vista para publicar un comentario en un producto.
class VistaPublicarComentario(SingleObjectMixin, FormView):
    model = Producto
    form_class = FormularioComentario
    template_name = 'gimnasio/detalle/detalle_producto.html'
    pk_url_kwarg = 'pk3'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comentario = form.save(commit = False)
        comentario.producto = self.object
        comentario.usuario = self.request.user
        comentario.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        producto = self.get_object()
        return reverse_lazy(
            'detalle_producto',
            kwargs = {
                'pk1': producto.categoria.categoria.pk,
                'pk2': producto.categoria.pk,
                'pk3': producto.pk
            }
        )

# Vista para agregar una categoría.
class VistaAgregarCategoria(CreateView):
    model = Categoria
    template_name = 'gimnasio/formularios/agregar_categoria.html'
    fields = '__all__'

# Vista para agregar una subcategoría.
class VistaAgregarSubcategoria(CreateView):
    model = Subcategoria
    template_name = 'gimnasio/formularios/agregar_subcategoria.html'
    fields = ['nombre', 'fotografia']

    def form_valid(self, form):
        form.instance.categoria = Categoria.objects.get(pk = self.kwargs['pk'])
        return super().form_valid(form)

# Vista para agregar un nuevo producto a una subcategoría.
class VistaAgregarProducto(CreateView):
    model = Producto
    template_name = 'gimnasio/formularios/agregar_producto.html'
    fields = ['nombre', 'descripcion', 'fotografia', 'precio', 'stock']

    def form_valid(self, form):
        form.instance.categoria = Subcategoria.objects.get(pk = self.kwargs['pk2'])
        return super().form_valid(form)

# Vista para modificar la información de una categoría.
class VistaEditarCategoria(UpdateView):
    model = Categoria
    template_name = 'gimnasio/formularios/editar_categoria.html'
    fields = '__all__'

# Vista para modificar la información de una subcategoría.
class VistaEditarSubcategoria(UpdateView):
    model = Subcategoria
    template_name = 'gimnasio/formularios/editar_subcategoria.html'
    pk_url_kwarg = 'pk2'
    fields = ['nombre', 'fotografia']
    
    def form_valid(self, form):
        form.instance.categoria = Categoria.objects.get(pk = self.kwargs['pk1'])
        return super().form_valid(form)

# Vista para modificar la información de un producto.
class VistaEditarProducto(UpdateView):
    model = Producto
    template_name = 'gimnasio/formularios/editar_producto.html'
    pk_url_kwarg = 'pk3'
    fields = ['nombre', 'descripcion', 'fotografia', 'precio', 'stock']

    def form_valid(self, form):
        form.instance.categoria = Subcategoria.objects.get(pk = self.kwargs['pk2'])
        return super().form_valid(form)

# Vista para eliminar una categoría.
class VistaEliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'gimnasio/formularios/eliminar_categoria.html'
    success_url = reverse_lazy('inicio')

# Vista para eliminar una subcategoría.
class VistaEliminarSubcategoria(DeleteView):
    model = Subcategoria
    template_name = 'gimnasio/formularios/eliminar_subcategoria.html'
    pk_url_kwarg = 'pk2'

    def get_success_url(self):
        subcategoria = self.get_object()

        return reverse_lazy(
            'lista_subcategorias',
            kwargs = {
                'pk': subcategoria.categoria.pk
            }
        )

# Vista para eliminar un producto.
class VistaEliminarProducto(DeleteView):
    model = Producto
    template_name = 'gimnasio/formularios/eliminar_producto.html'
    pk_url_kwarg = 'pk3'

    def get_success_url(self):
        producto = self.get_object()

        return reverse_lazy(
            'lista_productos',
            kwargs = {
                'pk1': producto.categoria.categoria.pk,
                'pk2': producto.categoria.pk
            }
        )