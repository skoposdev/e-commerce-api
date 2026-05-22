class CategoryCreateError(Exception): pass
class CategoryUpdateError(Exception): pass
class CategoryDeleteError(Exception): pass

class ProductCreateError(Exception): pass
class ProductUpdateError(Exception): pass
class ProductDeleteError(Exception): pass

class UserNotFoundError(Exception): pass
class UserCreateError(Exception): pass
class UserUpdateError(Exception): pass
class UserDeleteError(Exception): pass

class CartCreateError(Exception): pass

class CartItemsReturnedError(Exception): pass
class CartItemsCreateError(Exception): pass
class CartItemsUpdateError(Exception): pass
class CartItemsDeleteError(Exception): pass