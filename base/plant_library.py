from .models import libraryPlant 

cactus = libraryPlant.objects.create( name='Cactus', size='Small to Large', description='A succulent plant known for its spiky appearance and water-storing abilities.', inside=True, water='Infrequently', sun='Full sun to partial shade', fertilization='Occasionalfly', soil='Well-draining', pet=True ) 

peace_lily = libraryPlant.objects.create( name='Peace Lily', size='Medium', description='A popular indoor plant with glossy, dark green leaves and white flowers.', inside=True, water='Regularly', sun='Low to medium light', fertilization='Monthly', soil='Well-draining', pet=False ) 

haworthia = libraryPlant.objects.create( name='Haworthia', size='Small to Medium', description='A small succulent plant with rosette-shaped leaves.', inside=True, water='Infrequently', sun='Bright, indirect light', fertilization='Monthly', soil='Sandy or well-draining', pet=True ) 

snake_plant = libraryPlant.objects.create( name='Snake Plant', size='Medium to Large', description='A hardy indoor plant with long, upright leaves.', inside=True, water='Infrequently', sun='Low to bright indirect light', fertilization='Monthly', soil='Well-draining', pet=False ) 

pothos = libraryPlant.objects.create( name='Pothos', size='Medium', description='A vining plant with heart-shaped leaves that can be variegated.', inside=True, water='Regularly', sun='Low to medium light', fertilization='Monthly', soil='Well-draining', pet=True ) 

rubber_plant = libraryPlant.objects.create( name='Rubber Plant', size='Medium to Large', description='A popular indoor plant with large, glossy leaves.', inside=True, water='Regularly', sun='Bright, indirect light', fertilization='Monthly', soil='Well-draining', pet=False ) 

sunflower = libraryPlant.objects.create( name='Sunflower', size='Large', description='An annual plant known for its large, daisy-like flowers and tall stems.', inside=False, water='Regularly', sun='Full sun', fertilization='Weekly', soil='Well-draining', pet=False ) 

tomato = libraryPlant.objects.create( name='Tomato', size='Small to Large', description='A fruit-bearing plant commonly grown in gardens or containers.', inside=False, water='Regularly', sun='Full sun', fertilization='Bi-weekly', soil='Well-draining', pet=False ) 

cucumber = libraryPlant.objects.create( name='Cucumber', size='Medium to Large', description='A vining plant that produces elongated, green fruits used in salads and pickles.', inside=False, water='Regularly', sun='Full sun', fertilization='Weekly', soil='Well-draining', pet=False ) 

potato = libraryPlant.objects.create( name='Potato', size='Small to Large', description='A starchy tuberous crop widely cultivated for its edible underground tubers.', inside=False, water='Regularly', sun='Full sun', fertilization='Monthly', soil='Well-draining', pet=False ) 

orchid = libraryPlant.objects.create( name='Orchid', size='Small to Large', description='A diverse and widespread family of flowering plants with colorful and fragrant blooms.', inside=True, water='Regularly', sun='Indirect light', fertilization='Monthly', soil='Well-draining', pet=False ) 

spider_plant = libraryPlant.objects.create( name='Spider Plant', size='Small to Medium', description='An easy-to-grow houseplant with arching leaves and small white flowers.', inside=True, water='Regularly', sun='Indirect light', fertilization='Monthly', soil='Well-draining', pet=True ) 

zz_plant = libraryPlant.objects.create( name='ZZ Plant', size='Small to Medium', description='Zamioculcas zamiifolia, also known as the ZZ plant, is valued for its attractive, glossy green foliage and ability to tolerate low light conditions.', inside=True, water='Infrequently', sun='Low to indirect light', fertilization='Monthly', soil='Well-draining', pet=False ) 

philodendron = libraryPlant.objects.create( name='Philodendron', size='Small to Large', description='Philodendrons are popular indoor plants known for their lush, green foliage and easy care requirements. Varieties include heartleaf philodendron and Swiss cheese plant (Monstera deliciosa).', inside=True, water='Regularly', sun='Low to medium light', fertilization='Monthly', soil='Well-draining', pet=True ) 

boston_fern = libraryPlant.objects.create( name='Boston Fern', size='Medium', description='Nephrolepis exaltata, or Boston fern, is a classic indoor plant prized for its feathery fronds and ability to thrive in humid conditions. It adds a touch of lushness to any space.', inside=True, water='Regularly', sun='Indirect light', fertilization='Monthly', soil='Well-draining', pet=True ) 

aloe_vera = libraryPlant.objects.create( name='Aloe Vera', size='Small to Medium', description='Aloe vera is a succulent plant known for its medicinal properties and attractive, spiky leaves. It prefers bright, indirect light and infrequent watering.', inside=True, water='Infrequently', sun='Bright, indirect light', fertilization='Monthly', soil='Well-draining', pet=True ) 

hosta = libraryPlant.objects.create( name='Hosta', size='Medium to Large', description='Hostas are perennial plants valued for their attractive foliage, which comes in various shades of green, blue, or variegated patterns. They thrive in shady garden spots.', inside=False, water='Regularly', sun='Partial to full shade', fertilization='Monthly', soil='Moist, well-draining', pet=False )

gerbera_daisy = libraryPlant.objects.create( name='Gerbera Daisy', size='Small to Medium', description='Gerbera daisies are perennial flowering plants with large, colorful blooms. They are popular choices for adding a splash of color to garden beds or containers.', inside=False, water='Regularly', sun='Full sun to partial shade', fertilization='Bi-weekly', soil='Well-draining', pet=False ) 

hydrangea = libraryPlant.objects.create( name='Hydrangea', size='Medium to Large', description='Hydrangeas are deciduous shrubs prized for their large, showy flower heads that come in various shades of pink, blue, purple, or white. They prefer partial shade and moist, well-draining soil.', inside=False, water='Regularly', sun='Partial shade', fertilization='Monthly', soil='Moist, well-draining', pet=False ) 

marigold = libraryPlant.objects.create( name='Marigold', size='Small to Medium', description='Marigolds are annual flowering plants known for their bright orange, yellow, or red blooms. They are often used as bedding plants or in vegetable gardens to repel pests.', inside=False, water='Regularly', sun='Full sun', fertilization='Bi-weekly', soil='Well-draining', pet=False ) 

petunia = libraryPlant.objects.create( name='Petunia', size='Small to Medium', description='Petunias are annual flowering plants available in a wide array of colors. They are popular choices for adding color to garden beds, borders, and containers.', inside=False, water='Regularly', sun='Full sun', fertilization='Weekly', soil='Well-draining', pet=False ) 

geranium = libraryPlant.objects.create( name='Geranium', size='Small to Medium', description='Geraniums are flowering plants with colorful blooms that come in a variety of shapes and sizes. They are often used in containers, hanging baskets, or garden beds.', inside=False, water='Regularly', sun='Full sun to partial shade', fertilization='Bi-weekly', soil='Well-draining', pet=False ) 

lavender = libraryPlant.objects.create( name='Lavender', size='Small to Medium', description='Lavender is a fragrant herbaceous plant prized for its aromatic flowers and foliage. It\'s often used in gardens for its beauty and calming scent.', inside=False, water='Infrequently', sun='Full sun', fertilization='Monthly', soil='Well-draining', pet=False ) 

impatiens = libraryPlant.objects.create( name='Impatiens', size='Small to Medium', description='Impatiens are shade-loving annual plants with colorful flowers that bloom profusely throughout the summer. They are commonly used in containers or as ground cover in shaded areas.', inside=False, water='Regularly', sun='Partial to full shade', fertilization='Bi-weekly', soil='Well-draining', pet=False ) 

daylily = libraryPlant.objects.create( name='Daylily', size='Small to Medium', description='Daylilies are hardy perennial plants known for their colorful, trumpet-shaped flowers. They are easy to grow and come in a wide range of colors and sizes.', inside=False, water='Regularly', sun='Full sun to partial shade', fertilization='Monthly', soil='Well-draining', pet=False )

