# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
'''
>>> d = Dict(a=1, b=2)
>>> d['a']
1
>>> d.a
1
'''
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(fr"'Dict' object has no attribute '{key}'")
        
    def __setattr__(self, key, value):
        self[key] = value