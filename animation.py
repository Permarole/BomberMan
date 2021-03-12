import pygame


# Define a class that will handle animations
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # Start animation at first image
        self.images = animations.get(sprite_name)
        self.animation = False

    # method to start animation
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):

        # Check if animation is activated
        if self.animation:

            self.current_image += 1

            # check EOF
            if self.current_image >= len(self.images):
                # Reset animation
                self.current_image = 0

                # check if animation is not in loop mode
                if not loop :
                    self.animation = False

            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#TODO add exception if the file is not found
# load sprite's images
def load_animation_images(sprite_name,nb_image):
    # load nb_image images from the right file
    images = []
    # Get path
    path = f"assets/{sprite_name}/{sprite_name}"

    # Loop for every image
    for num in range(1, nb_image):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

def load_images(sprite_name):
    pass

def load_sprite_sheet(sprite_name,sprite_size,offset = (0,0)):
    """" Load a sprite sheet, sprite_size define how to subsurface the ss"""
    images = []
    # Get path
    path = f"assets/{sprite_name}.png"
    # Load the sprite sheet
    image = pygame.image.load(path)

    # Calculate the number of image for each row and each columns
    nbrows = image.get_width()//sprite_size[0]
    nbcols = image.get_height()//sprite_size[1]
    # Append each sprite to the list
    for col in range (nbcols):
        for row in range (nbrows):
            images.append(image.subsurface(((row*sprite_size[0],col*sprite_size[1]),sprite_size)))
    return images

# Create dictionary that will contain the images of every sprites
animations = {
    'bomber_black': load_sprite_sheet('bomber_black',(32,32)),
    'bomber_blue': load_sprite_sheet('bomber_blue',(32,32)),
    'bomber_green': load_sprite_sheet('bomber_green',(32,32)),
    'bomber_red': load_sprite_sheet('bomber_red',(32,32)),
    'bomber_white': load_sprite_sheet('bomber_white',(32,32)),
    'bomb': load_animation_images('bomb',6)
}
