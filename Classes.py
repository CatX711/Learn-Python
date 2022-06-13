# (this is a personal file so it wont be like a tutorial. For personal files that I myself can look at and read without the in depth writing my other tutorial files, there will
# be a disclaimer, like this one)


class Reptile:
    def Bite(self):
        print("Snap snap")
    def Lay_Egg(self):
        print("Squeeze!")


class Snake(Reptile):
    pass


class Python(Snake):
    pass


bite = Reptile()
bite.Bite()
bite.Lay_Egg()

      
