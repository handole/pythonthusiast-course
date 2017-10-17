# def print_args(a, b, c, *args):
# 		print(a, b, c, args)

# print_args(1,2,3,4,5)

# def print_kwargs(lat=None, long=None):
# 	print(lat, long)

# data = {'lat':0.01, 'long':1.02}

# print_kwargs(**data)

# def print_kwargs(lat=None, long=None, **kwargs):
# 	print(lat, long, kwargs)

# print_kwargs(1,2, data='other')

class Base(object):
	def __init__(self, *args, data=None, **kwargs):
		print('data is: ', data)
		print('kwargs are: ', kwargs)

class MyBaseObject(Base):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class MyObject(MyBaseObject):
	def __init__(self, *args, game=None, **kwargs):
		super().__init__(*args, **kwargs)
		print('game is: ', game)
