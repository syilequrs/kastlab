# Imports
import pygame, sys
from pygame.locals import *
import random, time
import pygame.transform

from pygame.sprite import Group
 
# Initialisation
pygame.init()
 
# Définition des FPS
FPS = 60
FramePerSec = pygame.time.Clock()
#Musique
tmusic = pygame.mixer_music.load("background.wav")
pygame.mixer.music.play(-1)
 
# Création des couleurs
BLEU  = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT  = (0, 255, 0)
NOIR  = (0, 0, 0)
BLANC = (255, 255, 255)
 
# Autres variables utilisées dans le programme
LARGEUR_ECRAN = 400
HAUTEUR_ECRAN = 600
VITESSE = 5
SCORE = 0
 
# Définition des polices
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, NOIR)
 
background = pygame.image.load("AnimatedStreet.png")

# Compteur de pièces et dernier moment où une pièce est apparue
COMPTEUR_PIECES = 0
dernier_temps_piece = pygame.time.get_ticks()
 
# Création d'un écran blanc
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(BLANC)
pygame.display.set_caption("Jeu")
 
class Ennemi(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, LARGEUR_ECRAN-40), 0)  
 
      def deplacer(self):
        global SCORE
        self.rect.move_ip(0, VITESSE)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, LARGEUR_ECRAN - 40), 0)
 
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def deplacer(self):
        touches_presseees = pygame.key.get_pressed()
      
        if self.rect.left > 0:
              if touches_presseees[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < LARGEUR_ECRAN:        
              if touches_presseees[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# Classe Pièce
class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, LARGEUR_ECRAN-40), 0)
    
    def deplacer(self):
        self.rect.move_ip(0, VITESSE)

# Création des sprites        
J1 = Joueur()
E1 = Ennemi()
P1 = Piece()
 
# Création des groupes de sprites
ennemis = pygame.sprite.Group()
ennemis.add(E1)

groupe_pieces = pygame.sprite.Group()
groupe_pieces.add(P1)

tous_les_sprites = pygame.sprite.Group()
tous_les_sprites.add(J1)
tous_les_sprites.add(E1)
tous_les_sprites.add(P1)
 
# Ajout d'un nouvel événement utilisateur
AUGMENTER_VITESSE = pygame.USEREVENT + 1
pygame.time.set_timer(AUGMENTER_VITESSE, 1000)
 
# Boucle de jeu
while True:
       
    # Parcours tous les événements en cours  
    for event in pygame.event.get():
        if event.type == AUGMENTER_VITESSE:
              VITESSE += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, NOIR)
    DISPLAYSURF.blit(scores, (10,10))
    pieces = font_small.render(str(COMPTEUR_PIECES), True, NOIR)
    DISPLAYSURF.blit(pieces, (370, 10))
 
    # Déplace et redessine tous les sprites
    for entity in tous_les_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.deplacer()
    
    # Logique de collecte des pièces
    if pygame.sprite.spritecollideany(J1, groupe_pieces):
        COMPTEUR_PIECES += 1
        entity.kill()  # Supprime la pièce

    # Logique de génération des pièces
    temps_actuel = pygame.time.get_ticks()
    if temps_actuel - dernier_temps_piece > 5000:
        nouvelle_piece = Piece()
        tous_les_sprites.add(nouvelle_piece)
        groupe_pieces.add(nouvelle_piece)
        dernier_temps_piece = temps_actuel  

    # À exécuter en cas de collision entre le joueur et un ennemi
    if pygame.sprite.spritecollideany(J1, ennemis):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(ROUGE)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in tous_les_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
