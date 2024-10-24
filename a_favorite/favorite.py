from a_users.models import Profile
from a_store.models import Product


class Favorite():

    def __init__(self, request):
        self.session = request.session
        self.request = request
        favorite = self.session.get('session_key2')

        if 'session_key2' not in request.session:
            favorite = self.session['session_key2'] = {}

        self.favorite = favorite

    def db_add(self, product):
        product_id = str(product_id)

        self.session.modified = True

        if self.session.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.user.id)
            favority = str(self.favorite)
            favority = favority.replace("\'", "\'")
            current_user.update(old_favorite=str(favority))

    def add(self, product):
        product_id = str(product.id)
        
        # Verifica si el producto ya está en los favoritos, si no, lo agrega
        if product_id not in self.favorite:
            self.favorite[product_id] = {'price': str(product.price)}

        # Marca la sesión como modificada para guardar los cambios
        self.session.modified = True

        # Si el usuario está autenticado, guarda la lista de favoritos en el perfil del usuario
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            favority = str(self.cart)
            favority = favority.replace("\'", "\"")  # Cambia comillas simples por dobles para JSON
            current_user.update(old_favorite=favority)


    def __len__(self):
        return len(self.favorite)

    def get_prods(self):
        product_ids = self.favorite.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    
    
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.favorite:
            del self.favorite[product_id]
            
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            favority = str(self.favorite)
            favority = favority.replace("\'", "\'")
            current_user.update(old_favorite=str(favority))