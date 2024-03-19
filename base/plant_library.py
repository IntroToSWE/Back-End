from .models import libraryPlant


# Create and save cactus plant
cactus = libraryPlant.objects.create(
    name='Cactus',
    size='Small to Large',
    description='A succulent plant known for its spiky appearance and water-storing abilities.',
    inside=True,
    water='Infrequently',
    sun='Full sun to partial shade',
    fertilization='Occasionalfly',
    soil='Well-draining',
    pet=True
)

# Create and save peace lily plant
peace_lily = libraryPlant.objects.create(
    name='Peace Lily',
    size='Medium',
    description='A popular indoor plant with glossy, dark green leaves and white flowers.',
    inside=True,
    water='Regularly',
    sun='Low to medium light',
    fertilization='Monthly',
    soil='Well-draining',
    pet=False
)

# Create and save haworthia plant
haworthia = libraryPlant.objects.create(
    name='Haworthia',
    size='Small to Medium',
    description='A small succulent plant with rosette-shaped leaves.',
    inside=True,
    water='Infrequently',
    sun='Bright, indirect light',
    fertilization='Monthly',
    soil='Sandy or well-draining',
    pet=True
)

# Create and save snake plant
snake_plant = libraryPlant.objects.create(
    name='Snake Plant',
    size='Medium to Large',
    description='A hardy indoor plant with long, upright leaves.',
    inside=True,
    water='Infrequently',
    sun='Low to bright indirect light',
    fertilization='Monthly',
    soil='Well-draining',
    pet=False
)

# Create and save pothos plant
pothos = libraryPlant.objects.create(
    name='Pothos',
    size='Medium',
    description='A vining plant with heart-shaped leaves that can be variegated.',
    inside=True,
    water='Regularly',
    sun='Low to medium light',
    fertilization='Monthly',
    soil='Well-draining',
    pet=True
)

# Create and save rubber plant
rubber_plant = libraryPlant.objects.create(
    name='Rubber Plant',
    size='Medium to Large',
    description='A popular indoor plant with large, glossy leaves.',
    inside=True,
    water='Regularly',
    sun='Bright, indirect light',
    fertilization='Monthly',
    soil='Well-draining',
    pet=False
)

print("Plants added to the database successfully!")
