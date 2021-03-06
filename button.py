import pygame.font


class Button:

    # noinspection PyTypeChecker
    def __init__(self, ai_settings, screen, msg, exit_msg):
        """初始化按钮"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)
        self.prep_exit(exit_msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_exit(self, exit_msg):
        self.exit_msg_image = self.font.render(exit_msg, True, self.text_color,
                                               self.button_color)
        self.exit_msg_image_rect = self.exit_msg_image.get_rect()
        self.exit_msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_exit_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.exit_msg_image, self.exit_msg_image_rect)
