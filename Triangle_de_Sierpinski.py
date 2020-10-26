import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(500,500)  # taille fenêtre graphique
turtle.pu()
turtle.goto(-0,-200)
turtle.pd()


def dessiner(courbe, longueur, angle):    
    #""" réalise une représentation graphique d'une courbe donnée par des chaines de caractères """
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere == 'F': turtle.forward(longueur)

def dessine_A(longueur, angle): 
  Sequence_A = 'FF++FF++FF++F+F++F++F+'
  dessiner(Sequence_A,longueur,angle)

def dessine_B(longueur, angle):
  Sequence_B = 'F++FF'
  dessiner(Sequence_B,longueur,angle)

def Prebienski(counter,longueur, angle):
  dessine_A(longueur,angle)
  for i in range(3):
    if counter>1:
      Prebienski(counter-1,longueur*0.5,angle)
  dessine_B(longueur,angle)
  return counter-1

longueur = 128
angle = 60
niter = 5

counter = niter;

if counter >= 0:
  counter = Prebienski(counter, longueur, angle)

turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique