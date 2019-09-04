'''
Crea un iterador personalizado que crea emojis
'''

import random

class CoolEmoticonGenerator(object):
    '''Clase que genea los emojis.'''
    strings = "!@#$^*_-=+?/,.:;~"
    grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]

    def create_emoticon(self, grp):
        '''Metodo que genera los emojis.'''
        face_strings_list = [random.choice(self.strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        return emoticon

    def __iter__(self):
        return self

    def __next__(self):
        grp = random.choice(self.grouped_strings)
        return self.create_emoticon(grp)

#from iterator_example import CoolEmoticonGenerator
g = CoolEmoticonGenerator()
print([next(g) for _ in range(5)])