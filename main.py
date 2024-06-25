import pygame
import sys
import random

#Funkce pro vytváření meteoritů na náhodných kordinátech nad zobrazenou plochou (záporné hodnoty 'y')
def generuj_meteor():
    return {
        "x": random.choice(range(10, 440, 50)),
        "y": random.choice(range(-10, -500, -50))
    }

if __name__ == "__main__":
    #Inicializace knihovny
    pygame.init()

    #Inicializace času
    clock = pygame.time.Clock()

    #Načtení obrázků do proměnných
    bg = pygame.image.load("assets/background.jpg")
    ship = pygame.image.load("assets/ship.png")
    meteor_img = pygame.image.load("assets/Meteor1.png")
    window = pygame.display.set_mode((500, 800))
    game_font = pygame.font.SysFont("comicsans", 30)

    #Nastavení základnich parametrů hry
    ship_coordinates_x = 220
    ship_coordinates_y = 700
    score = 0
    meteor_speed = 5
    meteor_count = 0
    meteor_increment = 4
    meteors = []



    while True:

        if len(meteors) == 0:
            meteor_speed += 0.5
            meteor_count += meteor_increment
            for i in range(meteor_count):
                meteors.append(generuj_meteor())
            

        score_text = game_font.render(f"Score {score}", True, (255, 255, 255))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        #Reakce lodi na mačkání kláves
        keys = pygame.key.get_pressed() #Proměnná pro uložení stisknutých kláves
        if keys[pygame.K_LEFT]:         #K_LEFT = šipka vlevo
            if ship_coordinates_x > 10: #Hrana za kterou se loď nedostane
                ship_coordinates_x -= 5 #Počet pixelů o které se loď pohne při stlačení šipky
        if keys[pygame.K_RIGHT]:
            if ship_coordinates_x < 410:
                ship_coordinates_x += 5
        







        #Vykreslování objektů
        window.blit(bg, (0, 0)) #pozadí
        window.blit(ship, (ship_coordinates_x, ship_coordinates_y)) #loď
        for meteor in meteors[:]: #meteory
            window.blit(meteor_img, (meteor['x'], meteor['y']))
            meteor["y"] += meteor_speed
            if meteor["y"] > 800:
                score += 1
                meteors.remove(meteor)
        window.blit(score_text, (350, 10)) #score


        pygame.display.update() #aktualizace obrazovky na konci cyklu

        clock.tick(60)
