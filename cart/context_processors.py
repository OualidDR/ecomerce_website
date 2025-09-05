from .cart import Cart

# create context processor so or cart can work on all pages 
def cart(request) :
    # return thedefault data from our Cart 
    return {'cart' :Cart(request)}
 