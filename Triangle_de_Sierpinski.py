import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(4000,4000)  # taille fenêtre graphique
turtle.pu()
turtle.goto(-150,-150)
turtle.pd()


def dessiner(courbe, longueur, angle):    
    """ réalise une représentation graphique d'une courbe donnée par des chaines de caractères """
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


def regleSierpinski(chaine):
    nouvelleChaine = ""    
    for lettre in chaine:  
        if lettre == "F":  
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  
        elif lettre == "G":
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre 
    return nouvelleChaine


def courbeSierpinski(motifInitial, niter):
    """ 
        appelle niter fois regleSierpinski pour créer la courbe de Sierpinski
    """
    courbe = motifInitial 
    for i in range(niter):
        nouveauMotif = regleSierpinski(courbe)  
        courbe = nouveauMotif 
    return courbe


longueur = 32
angle = -120
niter = 4


dessiner(courbeSierpinski('F-G-G', niter), longueur, angle)


turtle.update()    
turtle.exitonclick() 
