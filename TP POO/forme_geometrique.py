class Form:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

class Triangle(Form):
    def air(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        aire = (largeur*hauteur)/2
        print(aire)
    
class Rectangle(Form):
    def air(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        aire = largeur*hauteur
        print(aire)
    
triangle = Triangle(0,0)
triangle.air(51,51)
rectangle = Rectangle(0,0)
rectangle.air(51,51)
