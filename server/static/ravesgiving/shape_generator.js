
// first position number
function calc_x(){
    var x = -30;
    var x_coordinates = [];
    while (x<30) {
        x = x + 5
        x_cordinates.push(x);
    }
    return x_coordinates
}
// third position number
function calc_z(){
    var z = -30;
    var z_coordinates = [];
    while (z < 30) {
        z = z + 5;
        z_coordinates.push(z);
    }
    return z_coordinates
}

// second position number
y_coordinates = [2.8, 4.5, 3.5, 6.4, 3.2, 5.2];

function chooseRandom(list) {
    return list[Math.floor(Math.random() * list.length)]
}

var x_coordinates = calc_x()
var z_coordinates = calc_z()
// array to hold xyz coordinates
xyz_combos = []
// combine x and z coordinates
for (int i = 0 ; i != x_coordinates.length; i++) {
    var xyz = {
        x_coordinates[i] + ' '+ chooseRandom(y_coordinates) + ' ' +y_coordinates[i]
    }
    xyz_combos.push(xyz)
}


var colors = ['F266C1', '8B56BF', '716DF2', '91C5F2', 'A2F2EA', 'FFF287']
var rotations = ['0 0 0', '1.5 1.5 1.5', '7 8 -16', '15 90 0', '0 0 0']




// for(var i = 0; i < shapeVariations.length; i++){
//     createCone(shapeVariations[i].position, shapeVariations[i].color, shapeVariations[i].rotation);
//     createSphere(shapeVariations[i + 1].position)
// }

function* shapeGenerator() {
    while (true) {
        yield(createCone());
        // yield(createSphere());
        // yield(createBox());
    }
}

var shapeGen = shapeGenerator();
var shapes = ''

shapeVariations.forEach(function(variation) {
    // var shapeConstructor = shapeGen.next();
    var shape = shapeGen.next(variation.position, variation.color, variation.rotation);
    console.log(shape)
});




function createSphere(position, color, rotation) {
    var markup = `<a-sphere position="${position}" radius="1.25"
    rotation="${rotation}" scale="1 1 1" visible="true"
    material="color:#${color};metalness:0.34" geometry="primitive:sphere;radius:1">
    </a-sphere>`
}

function createBox(position, color, rotation) {
    var markup = `<a-box position="${position}" rotation="${rotation}" color="#4CC3D9"
    scale="1.5 1.5 1.5" visible="true" material="color:#${color};metalness:0.24"
    geometry="primitive:box">
        <a-animation easing="linear" attribute="rotation" dur="10000" to="0 60 0" repeat="indefinite">
        </a-animation>
    </a-box>`
}

function createCylinder(position, color, rotation) {
    var markup = `<a-cylinder position="${position}" radius="0.5" height="1.5"
    rotation="${rotation}" scale="1 1 1" visible="true"
    material="color:#${color};metalness:0.27"
    geometry="primitive:cylinder;radius:0.5;height:1.5"></a-cylinder>`
}

function createCone(position, color, rotation) {
    var markup = `<a-cone color="tomato" rotation="${rotation}" radius-bottom="2"
    radius-top="0.5" position="${position}" material="color:#${color}"
    geometry="height:1.67;radiusBottom:0.6;radiusTop:0"></a-cone>`
}
