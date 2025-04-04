import pygame, random, time

pygame.init()

#settings
screen_width = 600
screen_height = 400
snake_size = 10
food_size = 10
initial_speed = 10
FPS = 60
speed_multiplier = 1

#colours
white = (255, 255, 255)
black = (0, 0, 0)
bright_green = (0, 255, 0)
dark_green = (45, 155, 61)
red = (255, 0, 0)

#font
font = pygame.font.SysFont(None, 30)

#window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ulitka")
clock = pygame.time.Clock()

#food types
foodtype = [
    {"colour": (255, 0, 0), "weight": 1, "lifespan": float('inf')},
    {"colour": (0, 0, 255), "weight": 2, "lifespan": 10000},
    {"colour": (255, 255, 0), "weight": 5, "lifespan": 5000},
]

def display_text(text, color, x, y):
    message = font.render(text, True, color)
    screen.blit(message, [x, y])

def draw_snake(snake_list):
    for index, (x, y) in enumerate(snake_list):
        color = bright_green if index % 2 == 0 else dark_green
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])

def generate_food(snake_list):
    while True:
        food_x = random.randrange(0, screen_width - food_size, 10)
        food_y = random.randrange(0, screen_height - food_size, 10)
        if (food_x, food_y) not in snake_list:
            food = random.choice(foodtype)
            return {
                "x": food_x, 
                "y": food_y,
                "colour": food["colour"],
                "weight": food["weight"],
                "lifespan": food["lifespan"],
                "spawn_time": pygame.time.get_ticks()
            }

def game_over_screen():
    screen.fill(black)
    display_text("Skill issue? da/net", red, screen_width / 3, screen_height / 3)
    pygame.display.update()

def game_loop():
    game_running = True
    game_close = False
    
    x, y = screen_width // 2, screen_height // 2
    x_change, y_change = 0, 0
    move_counter = 0 
    
    snake_list = []
    snake_length = 1
    food = generate_food(snake_list)
    
    score = 0
    level = 1
    speed = initial_speed
    
    while game_running:
        currenttime = pygame.time.get_ticks()

        #expiration date
        if food["lifespan"] != float('inf') and currenttime - food["spawn_time"] > food["lifespan"]:
            food = generate_food(snake_list)

        while game_close:
            game_over_screen()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:  # restart
                        return game_loop()
                    elif event.key == pygame.K_y:  # quit
                        pygame.quit()
                        quit()
        
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change, y_change = -snake_size, 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change, y_change = snake_size, 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change, y_change = 0, -snake_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change, y_change = 0, snake_size
        
        # spdprecise
        move_counter += speed_multiplier
        if move_counter >= FPS / speed:
            move_counter = 0
            
            # mexico
            if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
                game_close = True
            
            x += x_change
            y += y_change
            
            screen.fill(black)
            pygame.draw.rect(screen, food["colour"], [food["x"], food["y"], food_size, food_size])  # draw food
            
            snake_list.append((x, y))
            if len(snake_list) > snake_length:
                del snake_list[0]
            
            # selfharm
            if (x, y) in snake_list[:-1]:
                game_close = True
            
            draw_snake(snake_list)
            display_text(f"Score: {score}", white, 10, 10)
            display_text(f"Level: {level}", white, 10, 40)
            
            pygame.display.update()
            
            # eating food
            if x == food["x"] and y == food["y"]:
                food = generate_food(snake_list)
                snake_length += 1
                score += food["weight"]
                
                if score % 5 == 0:  # lvl advancement
                    level += 1
                    speed += 1  
        
        clock.tick(FPS)
    
    pygame.quit()
    quit()

game_loop()
