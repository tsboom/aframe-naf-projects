#python
from bs4 import BeautifulSoup
from jinja2 import Template
import round
import random
import itertools
import pdb



def calc_x():
    # find the coordinates to loop through later
    # first number (negative is left and positive is right)
    x = -50
    x_coordinates = []
    while (x < 50):
        x = x + 8
        x_coordinates.append(x)
    return x_coordinates

# third number (+ up and  - down)
def calc_z():
    z = -50
    z_coordinates = []
    while (z < 50):
        z = z + 8
        z_coordinates.append(z)
    return z_coordinates



# second number (height: positive is above the floor)
def getRandomHeight():
    y = round(random.uniform(2, 7), 2)
    return y

# alternative height list
y_coordinates = [2.8, 4.5, 3.5, 6.4, 7.2, 5.2, 8]

x_coordinates = calc_x()
z_coordinates = calc_z()

# combine x and z coordinates
xz_combos = [[x, z] for x in x_coordinates for z in z_coordinates]

# array to hold xyz coordinates
xyz_combos = []
# add z per coordinate combo
for combo in xz_combos:
    y = random.choice(y_coordinates)
    combo.insert(1, y)
    xyz_combos.append(str(combo[0]) +' '+ str(combo[1]) +' '+ str(combo[2]))

def shape_attr_generator(dataset):
    count = 0
    while True:
        # reset counter when needed
        if count > len(dataset):
            count = 0
        # return the next color in the list
        yield dataset[count]
        count = count + 1

colors = ['F266C1', '8B56BF', '716DF2', '91C5F2', 'A2F2EA', 'FFF287', '8B56BF', 'F266C1', '9CF55E', 'A2F2EA']
rotations = ['0 0 0', '1.5 1.5 1.5', '7 8 -16', '15 90 0', '0 0 0']
# color_gen = shape_attr_generator(colors)
# rotation_gen = shape_attr_generator(rotations)
#
# # Build a list of shape variations
# shape_variations = []
#
# for xyz in xyz_combos:
#     shape_variation = {
#         "position": xyz,
#         "rotation": rotation_gen.next(),
#         "color": color_gen.next()
#     }
#     shape_variations.append(shape_variations)


#all_zipped = [[xyz, c, r] for xyz, c, r in zip(xyz_combos, itertools.cycle(colors), itertools.cycle(rotations))]
all_zipped = [{'position': xyz, 'color':c, 'rotation':r} for xyz, c, r in zip(xyz_combos, itertools.cycle(colors), itertools.cycle(rotations))]
print all_zipped
# print shape_variations

# template = Template(
# {% for xyz, c, r in all_zipped %}
# <a-sphere position="{{xyz[0]}} {{xyz[1]}} {{xyz[2]}}" radius="1.25"  rotation="{{ r "}} scale="1 1 1" visible="true" material="color:#{{ c }};metalness:0.34" geometry="primitive:sphere;radius:1"></a-sphere>
# <a-box position="-1.052 2.922 -7.221" rotation="-0.77 5835.55" color="#4CC3D9" scale="1.5 1.5 1.5" visible="true" material="color:#66ffcc;metalness:0.24" geometry="primitive:box">
#     <a-animation easing="linear" attribute="rotation" dur="10000" to="0 60 0" repeat="indefinite"></a-animation>
# </a-box>
# <a-cylinder position="9.077 3.283 -6.018" radius="0.5" height="1.5" color="#FFC65D" rotation="7 8 -16" scale="1 1 1" visible="true" material="color:#ccff66;metalness:0.27" geometry="primitive:cylinder;radius:0.5;height:1.5"></a-cylinder>
# <a-cone color="tomato" rotation="15 90 0" radius-bottom="2" radius-top="0.5" position="-4 7 -5" material="color:#400080" geometry="height:1.67;radiusBottom:0.6;radiusTop:0"></a-cone>
# {% endfor %}
# )
