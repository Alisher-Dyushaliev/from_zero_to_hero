class Mixin (object):
    mix_prop = ''

    def get_prop (self):
        return self.mix_prop.upper()

    def get_upper (self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()