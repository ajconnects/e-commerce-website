
class Cart():
    def __init__(self, request) -> None:
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new, no session key! create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all page of sites
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        #logic of adding product
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)