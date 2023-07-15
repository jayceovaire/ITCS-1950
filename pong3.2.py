import random
import pygame


class Player():
        """added name argument to init and added an if else block to set starting positions """
        def __init__(self, name, SCR_WID, SCR_HEI):
                self.speed = 4
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
                self.name = name
                self.ability_active = False
                self.ability_filled = False
                self.initial_padHei = self.padHei
                self.ability_cooldown = 15000
                self.ability_duration = 5000
                self.ability_start_time = 0
                self.ability_bar_fill_color = (255, 255, 255)
                self.ability_one = False
                self.ability_two = False
                self.ability_three = False
                
                if name == 'player':
                        self.x, self.y = self.padWid + 16 , SCR_HEI/2
                elif name == 'enemy':
                        self.x, self.y = SCR_WID - self.padWid - 25, SCR_HEI / 2
                elif name == 'bottom':
                        self.x, self.y = SCR_WID / 2, 465
                        self.padWid, self.padHei = 64, 8
                elif name == 'middle':
                        self.x, self.y = SCR_WID / 2 - self.padWid / 2 + 1, SCR_HEI / 2 - self.padHei / 2

        def scoring(self, screen, SCR_HEI, SCR_WID):
                enemy_wins = self.scoreFont.render('Player 2 Wins!', 1, (255, 255, 255))
                player_wins = self.scoreFont.render('Player 1 Wins!', 1, (255, 255, 255))
                play_again_text = self.scoreFont.render('Play Again?', 1, (255, 255, 255))
                yes_text = self.scoreFont.render('< Yes >', 1, (255, 255, 255))
                no_text = self.scoreFont.render('< No >', 1, (255, 255, 255))
                if self.name == 'player':
                        scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                        screen.blit(scoreBlit, (32, 16))
                        if self.score == 10:
                                screen.blit(player_wins, (SCR_WID // 2 - player_wins.get_width() // 2, SCR_HEI // 2))
                                pygame.display.update()
                                pygame.time.delay(3000)
                                print("player 1 wins!")
                                screen.fill((0,0,0))
                                screen.blit(play_again_text, (SCR_WID // 2 - play_again_text.get_width() // 2, SCR_HEI // 2))
                                screen.blit(yes_text, (SCR_WID // 2 - yes_text.get_width() // 2, SCR_HEI + play_again_text.get_height()))
                                pygame.display.update()
                                keys = pygame.key.get_pressed()
                                yes_selected = True
                                just_switched = False

                                while True:
                                        keys = pygame.key.get_pressed()
                                        screen.fill((0,0,0))
                                        screen.blit(play_again_text, (SCR_WID // 2 - play_again_text.get_width() // 2, SCR_HEI // 2))

                                        if yes_selected:
                                                screen.blit(yes_text, (SCR_WID // 2 - yes_text.get_width() // 2, SCR_HEI // 2 + play_again_text.get_height()))
                                        else:
                                                screen.blit(no_text, (SCR_WID // 2 - no_text.get_width() // 2, SCR_HEI // 2 + play_again_text.get_height()))

                                        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and not just_switched:
                                                yes_selected = not yes_selected
                                                just_switched = True

                                        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                                                just_switched = False

                                        pygame.display.update()

                                        if keys[pygame.K_RETURN]:
                                                if yes_selected:
                                                        main()
                                                else:
                                                        exit()
                                        for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                        exit()

                                
                elif self.name == 'enemy':
                        scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                        screen.blit(scoreBlit, (SCR_HEI + 92, 16))
                        if self.score == 10:
                                screen.blit(enemy_wins, (SCR_WID // 2 - player_wins.get_width() // 2, SCR_HEI // 2))
                                pygame.display.update()
                                pygame.time.delay(3000)
                                print("Player 2 wins!")
                                screen.fill((0,0,0))
                                screen.blit(play_again_text, (SCR_WID // 2 - play_again_text.get_width() // 2, SCR_HEI // 2))
                                screen.blit(yes_text, (SCR_WID // 2 - yes_text.get_width() // 2, SCR_HEI + play_again_text.get_height()))
                                pygame.display.update()
                                keys = pygame.key.get_pressed()
                                yes_selected = True
                                just_switched = False
                                
                                while True:
                                        keys = pygame.key.get_pressed()
                                        screen.fill((0,0,0))
                                        screen.blit(play_again_text, (SCR_WID // 2 - play_again_text.get_width() // 2, SCR_HEI // 2))

                                        if yes_selected:
                                                screen.blit(yes_text, (SCR_WID // 2 - yes_text.get_width() // 2, SCR_HEI // 2 + play_again_text.get_height()))
                                        else:
                                                screen.blit(no_text, (SCR_WID // 2 - no_text.get_width() // 2, SCR_HEI // 2 + play_again_text.get_height()))

                                        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and not just_switched:
                                                yes_selected = not yes_selected
                                                just_switched = True
                                        
                                        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                                                just_switched = False

                                        pygame.display.update()

                                        if keys[pygame.K_RETURN]:
                                                if yes_selected:
                                                        main()
                                                else:
                                                        exit()
                                        for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                        exit()
                                        

        def movement(self, SCR_HEI, ball=None):
                # movement keys are now dependent upon the name of the player 'player' or 'enemy'
                keys = pygame.key.get_pressed()
                current_time = pygame.time.get_ticks()
                
                if self.name == 'player':
                        if keys[pygame.K_w]:
                                self.y -= self.speed
                        elif keys[pygame.K_s]:
                                self.y += self.speed
                        # After 15 seconds and every 15 seconds after ability is used and goes off cooldown the player can activate
                        # their ability in order to increase paddle length and speed
                        if keys[pygame.K_LCTRL] and self.ability_filled and not self.ability_active:
                                self.ability_active = True
                                self.ability_one = True
                                self.ability_start_time = current_time
                                
                        if self.ability_active and self.ability_one:
                                self.padHei = 100
                                self.speed = 6
                                # keeps track of 5 second ability duration then resets paddle attributes
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 4
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_one = False
                        
                        if keys[pygame.K_a] and self.ability_filled and not self.ability_active:
                                # second player ability grows the paddle to a length of 200 and keeps original speed
                                self.ability_active = True
                                self.ability_two = True
                                self.ability_start_time = current_time
                                
                        if self.ability_active and self.ability_two:
                                self.padHei = 200
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 3
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_two = False
                        if keys[pygame.K_d] and self.ability_filled and not self.ability_active:
                                self.ability_active = True
                                self.ability_three = True
                                self.ability_start_time = current_time
                        if self.ability_active and self.ability_three:
                                self.padHei = 50
                                self.speed = 10
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 4
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_three = False
                        if not self.ability_active:
                                # keeps track of 15 second cooldown timer
                                if current_time - self.ability_start_time >= 15000:
                                        self.ability_filled = True
                                self.padHei = self.initial_padHei
                                self.speed = 4
                                self.ability_one = False
                                self.ability_two = False
                                self.ability_three = False
                        
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                                
                                
                if self.name == 'enemy':
                        if keys[pygame.K_UP]:
                                self.y -= self.speed
                        elif keys[pygame.K_DOWN]:
                                self.y += self.speed
                                
                        # same ability code as above        
                        if keys[pygame.K_RCTRL] and self.ability_filled and not self.ability_active:
                                self.ability_active = True
                                self.ability_one = True
                                self.ability_start_time = current_time
                        if self.ability_active and self.ability_one:
                                self.padHei = 100
                                self.speed = 6
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 4
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_one = False
                        
                        if keys[pygame.K_RIGHT] and self.ability_filled and not self.ability_active:
                                self.ability_active = True
                                self.ability_two = True
                                self.ability_start_time = current_time
                        if self.ability_active and self.ability_two:
                                self.padHei = 200
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 3
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_two = False
                       
                        if keys[pygame.K_LEFT] and self.ability_filled and not self.ability_active:
                                self.ability_active = True
                                self.ability_three = True
                                self.ability_start_time = current_time
                        if self.ability_active and self.ability_three:
                                self.padHei = 50
                                self.speed = 10
                                if current_time - self.ability_start_time >= self.ability_duration:
                                        self.padHei = self.initial_padHei
                                        self.speed = 4
                                        self.ability_filled = False
                                        self.ability_active = False
                                        self.ability_three = False
                        if not self.ability_active:
                                # keeps track of 15 second cooldown timer
                                if current_time - self.ability_start_time >= 15000:
                                        self.ability_filled = True
                                self.padHei = self.initial_padHei
                                self.speed = 4
                                self.ability_one = False
                                self.ability_two = False
                                self.ability_three = False
                                

                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                                
                if self.name == 'bottom':
                        self.x = ball.x - self.padWid / 2

                if self.name == 'middle':
                        self.y += self.speed
                        if self.y <= 0:
                                self.speed *= -1
                        elif self.y >= SCR_HEI - self.padHei:
                                self.speed *= -1



        def draw(self, screen):
                if self.name == 'middle':
                        pygame.draw.rect(screen, (150, 0, 150), (self.x, self.y, self.padWid, self.padHei))
                        
                else:
                        # when ability is ready to use the paddles will turn gold
                        if self.ability_filled:
                                self.ability_bar_fill_color = (255, 200, 0)
                        else:
                                # if ability is not ready to use the paddles will be white
                                self.ability_bar_fill_color = (255, 255, 255)
                        pygame.draw.rect(screen, self.ability_bar_fill_color, (self.x, self.y, self.padWid, self.padHei))
                        
                        


class Ball():
        def __init__(self, SCR_WID, SCR_HEI):
                # Ball randomly __init__ almost anywhere on the screen
                self.x, self.y = random.randint(50, SCR_WID - 50), random.randint(100, SCR_HEI - 50)
                # RNG to dictate whether the ball is moving upward or downward / left or right when it inits
                random_movement = random.randint(1, 2)
                if random_movement == 1:
                        self.speed_x = -3
                        self.speed_y = 3
                elif random_movement == 2:
                        self.speed_x = 3
                        self.speed_y = -3
                self.size = 8

        def movement(self, player, enemy, bottom_paddle, SCR_WID, SCR_HEI, BALL_BOUNCE_SOUNDS, middle_paddle,
                     MIDDLE_PADDLE_ACTIVE, TOTAL_SCORE):
                self.x += self.speed_x
                self.y += self.speed_y

                # wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI - self.size:
                        self.speed_y *= -1

                if self.x <= 0:
                        self.__init__(SCR_WID, SCR_HEI)
                        enemy.score += 1
                elif self.x >= SCR_WID - self.size:
                        self.__init__(SCR_WID, SCR_HEI)
                        self.speed_x = 3
                        player.score += 1
                ##wall col
                # paddle col
                # player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        #when ball bounces off paddle it plays the bounce sound
                                        BALL_BOUNCE_SOUNDS.play()
                                        # while the total score of the players is below 3 the balls get faster with each bounce
                                        # in order to prevent the game from going on as 0 - 0 forever before the difficuly is increased at 3, 6, 9, 12 points
                                        if TOTAL_SCORE < 6:
                                                self.speed_x += 1 if self.speed_x > 0 else - 1
                                                self.speed_y += 1 if self.speed_y > 0 else - 1
                                        break
                        n += 1
                # enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                        self.speed_x *= -1
                                        BALL_BOUNCE_SOUNDS.play()
                                        if TOTAL_SCORE < 6:
                                                self.speed_x += 1 if self.speed_x > 0 else - 1
                                                self.speed_y += 1 if self.speed_y > 0 else - 1
                                        break
                        n += 1

                ##bottom_paddle col
                for n in range(-self.size, bottom_paddle.padWid):
                        if self.y == bottom_paddle.y + n:
                                self.speed_y *= -1
                                BALL_BOUNCE_SOUNDS.play()
                                if TOTAL_SCORE < 4:
                                        self.speed_y += 1 if self.speed_y > 0 else -1
                                break
                        n += 1

                # middle paddle
                if MIDDLE_PADDLE_ACTIVE:
                        for n in range(-self.size, middle_paddle.padHei):
                                if self.y == middle_paddle.y + n:
                                        if self.x >= middle_paddle.x - self.size and self.x <= middle_paddle.x + middle_paddle.padWid:
                                                self.speed_y *= -1
                                                self.speed_x *= -1
                                                BALL_BOUNCE_SOUNDS.play()
                                                if TOTAL_SCORE < 6 or TOTAL_SCORE > 10:
                                                        self.speed_x += 1 if self.speed_x > 0 else -1
                                                        self.speed_y += 1 if self.speed_y > 0 else -1
                                                break
                                                

        def draw(self,screen):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))


class Buff():
        """randomly spawning ball (de)buffs that will either double or halve the size of the ball colliding with it"""
        def __init__(self, SCR_WID, SCR_HEI):
                self.x = random.randint(100, SCR_WID - 100)
                self.y = random.randint(100, SCR_HEI - 100)
                self.size = 30
                self.type = random.choice(['double', 'halve'])
                self.color = (255, 0, 0) if self.type == "double" else (0, 0, 255)
                self.spawn_time = pygame.time.get_ticks()
                
        def draw(self, screen):
                pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

def main():
        """moved all logic and variables to main() and passed variables to objects for their methods / init"""
        #starts pygame and pygame music mixer
        pygame.init()
        pygame.mixer.init()
        SCR_WID, SCR_HEI = 640, 480
        #Background image constant
        BACKGROUND = pygame.transform.scale(pygame.image.load('pong_background.png'), (SCR_WID, SCR_HEI))
        screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
        pygame.display.set_caption("Pong")
        pygame.font.init()
        clock = pygame.time.Clock()
        FPS = 60
        scoreFont = pygame.font.Font("imagine_font.ttf", 64)
        # music / sounds
        music_file = 'background_music.wav'
        BALL_BOUNCE_SOUNDS = pygame.mixer.Sound('ball_bounce.wav')
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)

        #keeps track of if the music is playing or stopped
        MUSIC_PLAYING = True
        # used to decide when to switch music tracks
        music_changer = True
        
        # paddles
        player = Player('player', SCR_WID, SCR_HEI)
        enemy = Player('enemy', SCR_WID, SCR_HEI)
        bottom_paddle = Player('bottom', SCR_WID, SCR_HEI)
        middle_paddle = Player('middle', SCR_WID, SCR_HEI)
        MIDDLE_PADDLE_ACTIVE = False
        # balls
        ball = Ball(SCR_WID, SCR_HEI)
        ball2 = Ball(SCR_WID, SCR_HEI)
        ball3 = Ball(SCR_WID, SCR_HEI)
        
        # list of buffs on screen
        buffs = []
        #timer for next buff time of current game length + 10 seconds
        next_buff_time = pygame.time.get_ticks() + 10000
        # Game Pause booleans
        GAME_PAUSED = False
        #keeps track of pause key
        just_unpaused = False
        #keeps track of main menu status for replay game
        MAIN_MENU = True
        # keeps track of whether the main menu is on < start > 
        START_SCREEN = True
        # keeps track of whether the main menu is on < controls >
        CONTROLS_SCREEN = False
        # keeps track of left and right key presses
        just_switched = False
        #keeps tracks of whether the controls are being presented after the < controls > screen
        controls_displayed = False
        # also keeps track of controls being displayed - used to prevent rapid hopping from < controls > to the controls text
        just_pressed_return = False
        
        while True:
                # process
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print("Game exited by user")
                                exit()
                                
                while MAIN_MENU:
                        screen.fill((0, 0, 0))

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print("Game exited by user")
                                        exit()
                                        
                        keys = pygame.key.get_pressed()
                        if START_SCREEN:
                                menu_text = scoreFont.render("< Start Game >", 1, (255, 255, 255))
                                menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))

                                if keys[pygame.K_RETURN]:
                                        # Game countdown to start 5 , 4, 3, 2, 1, play!
                                        screen.fill((0,0,0))
                                        pygame.display.update()
                                        menu_text = scoreFont.render("5", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        screen.fill((0,0,0))
                                        pygame.time.wait(1000)
                                        menu_text = scoreFont.render("4", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        screen.fill((0,0,0))
                                        pygame.time.wait(1000)
                                        menu_text = scoreFont.render("3", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        screen.fill((0,0,0))
                                        pygame.time.wait(1000)
                                        menu_text = scoreFont.render("2", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        screen.fill((0,0,0))
                                        pygame.time.wait(1000)
                                        menu_text = scoreFont.render("1", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        screen.fill((0,0,0))
                                        pygame.time.wait(1000)
                                        menu_text = scoreFont.render("PLAY!", 1, (255, 255, 255))
                                        menu_screen = screen.blit(menu_text, (SCR_WID // 2 - menu_text.get_width() // 2, SCR_HEI // 2))
                                        pygame.display.update()
                                        pygame.time.wait(500)
                                        MAIN_MENU = False
                                        # breaks loop to allow game to start
                                        break

                                if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                                        if not just_switched:
                                                START_SCREEN = False
                                                CONTROLS_SCREEN = True
                                                just_switched = True
                                elif not keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                                        just_switched = False
                                
                        
                        elif CONTROLS_SCREEN and not controls_displayed:
                                controls_text = scoreFont.render("< Controls >", 1, (255, 255, 255))
                                menu_screen = screen.blit(controls_text, (SCR_WID // 2 - controls_text.get_width() // 2, SCR_HEI // 2))
                                
                                
                                if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                                        if not just_switched:
                                                START_SCREEN = True
                                                CONTROLS_SCREEN = False
                                                just_switched = True
                                                
                                elif not keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                                        just_switched = False
                                        
                                if keys[pygame.K_RETURN] and not controls_displayed and not just_pressed_return:
                                        controls_displayed = True
                                        just_pressed_return = True
                                if not keys[pygame.K_RETURN]:
                                        just_pressed_return = False
                                        
                                
                        
                        elif CONTROLS_SCREEN and controls_displayed:
                                smallFont = pygame.font.Font("imagine_font.ttf", 16)
                                control_lines = [
                                        "UP/DOWN/W/S =  Move up and Move down",
                                        "LCTRL / RCTRL = Grow paddle and increase speed",
                                        "A/RIGHT_ARROW = Giant paddle and lower speed",
                                        "D/LEFT_ARROW = Small paddle and greatly increase speed",
                                        "Pause Game with P",
                                        "When paddles are gold you can use specials",
                                        "Press enter to return to main menu"
                                ]

                                y_offset = 0
                                for line in control_lines:
                                        control = smallFont.render(line, 1, (255, 255, 255))
                                        screen.blit(control, (SCR_WID // 2 - control.get_width() // 2, SCR_HEI // 2 + y_offset))
                                        y_offset += control.get_height() + 5 
                                pygame.display.update()
                                        
                                if keys[pygame.K_RETURN] and not just_pressed_return:
                                        controls_displayed = False
                                        just_pressed_return = True
                                        
                                elif not keys[pygame.K_RETURN]:
                                        just_pressed_return = False
                                                
                        pygame.display.update()
                        pygame.time.Clock().tick(60) 

                                
                # Game Pause Logic
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p] and not GAME_PAUSED and not just_unpaused:
                        GAME_PAUSED = True
                        just_unpaused = True
                        
                        while GAME_PAUSED:
                                for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                                pygame.quit()
                                                exit()
                                        
                                        keys = pygame.key.get_pressed()
                                        if keys[pygame.K_p]:
                                                GAME_PAUSED = False
                                                just_unpaused = True
                                                
                                pause_text = scoreFont.render("Game Paused", 1, (255, 255, 255))
                                pause_screen = screen.blit(pause_text, (SCR_WID // 2 - pause_text.get_width() // 2, SCR_HEI // 2))
                                pygame.display.flip()
                                pygame.time.Clock().tick(60)
                                
                elif not keys[pygame.K_p]:
                        # when p key is released the just_unpaused control is reset so the game wont register more than one keydown
                        just_unpaused = False
                                
                # when game time reaches next buff time, spawn buff then recalculate next buff spawn time                
                if pygame.time.get_ticks() >= next_buff_time:
                        buffs.append(Buff(SCR_WID, SCR_HEI))
                        next_buff_time = pygame.time.get_ticks() + 10000
                        
                # buff collision checks        
                for buff in buffs:
                        if ball.x < buff.x + buff.size and ball.x + ball.size > buff.x and ball.y < buff.y + buff.size and ball.y + ball.size > buff.y:
                                if buff.type == "double":
                                        ball.size = round(ball.size * 2)
                                else:
                                        ball.size = round(ball.size / 2)
                                buffs.remove(buff)
                        if ball2.x < buff.x + buff.size and ball2.x + ball2.size > buff.x and ball2.y < buff.y + buff.size and ball2.y + ball2.size > buff.y:
                                if buff.type == "double":
                                        ball2.size = round(ball2.size * 2)
                                else:
                                        ball2.size = round(ball2.size / 2)
                                buffs.remove(buff)
                
                        if ball3.x < buff.x + buff.size and ball3.x + ball3.size > buff.x and ball3.y < buff.y + buff.size and ball3.y + ball3.size > buff.y:
                                if buff.type == "double":
                                        ball3.size = round(ball3.size * 2)
                                else:
                                        ball3.size = round(ball3.size / 2)
                                buffs.remove(buff)
                                
                                 
                ##process
                # logic
                # keeps track of combined player scores to set difficulty
                TOTAL_SCORE = player.score + enemy.score
                
                ball.movement(player, enemy, bottom_paddle, SCR_WID, SCR_HEI, BALL_BOUNCE_SOUNDS, middle_paddle, MIDDLE_PADDLE_ACTIVE, TOTAL_SCORE)
                player.movement(SCR_HEI)
                enemy.movement(SCR_HEI)
                bottom_paddle.movement(SCR_HEI, ball)
                ##logic
                # draw
                #fills screen black between frames to prevent ball ghosting
                screen.fill((0, 0, 0))
                #displays background before ball is drawn
                screen.blit(BACKGROUND, (0, 0))
                ball.draw(screen)
                player.draw(screen)
                player.scoring(screen, SCR_HEI, SCR_WID)
                enemy.draw(screen)
                enemy.scoring(screen, SCR_HEI, SCR_WID)
                bottom_paddle.draw(screen)
                
                #  draw buffs on screen
                for buff in buffs:
                        buff.draw(screen)
                
                if TOTAL_SCORE == 3 and music_changer is True:
                        music_changer = False
                        MUSIC_PLAYING = False

                if TOTAL_SCORE >= 3:
                        # adds middle paddle to game
                        MIDDLE_PADDLE_ACTIVE = True
                        middle_paddle.draw(screen)

                if TOTAL_SCORE >= 6:
                        ball2.draw(screen)
                        ball2.movement(player, enemy, bottom_paddle, SCR_WID, SCR_HEI, BALL_BOUNCE_SOUNDS, middle_paddle, MIDDLE_PADDLE_ACTIVE, TOTAL_SCORE)
                if TOTAL_SCORE >= 9:
                        #middle paddle starts moving
                        middle_paddle.movement(SCR_HEI)
                        
                if TOTAL_SCORE >= 12:
                        #adds 3rd ball to game
                        ball3.draw(screen)
                        ball3.movement(player, enemy, bottom_paddle, SCR_WID, SCR_HEI, BALL_BOUNCE_SOUNDS, middle_paddle, MIDDLE_PADDLE_ACTIVE, TOTAL_SCORE)
                        

                #changes music to second file
                if TOTAL_SCORE == 3 and MUSIC_PLAYING is False:
                        pygame.mixer.music.stop()
                        music_file = "background_music_two.wav"
                        pygame.mixer.music.load(music_file)
                        pygame.mixer.music.play(-1)
                        MUSIC_PLAYING = True

                ##draw
                # _______
                pygame.display.flip()
                clock.tick(FPS)


if __name__ == '__main__':
        main()
        