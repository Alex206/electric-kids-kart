// Parametric concept model. Dimensions in mm.
// Update from calculations/defaults.json after measuring actual wheels.

frame_length = 1600;
frame_width = 760;
wheelbase = 1100;
front_track = 820;
rear_track = 780;
rear_wheel_d = 300;
front_wheel_d = 280;
wheel_width = 100;
ground_clearance = 65;
main_tube = 30;
secondary_tube = 25;

module beam_x(x, y, z, len, size=main_tube) {
    translate([x, y, z]) cube([len, size, size]);
}
module beam_y(x, y, z, len, size=main_tube) {
    translate([x, y, z]) cube([size, len, size]);
}
module wheel(x, y, z, d, width) {
    translate([x, y, z]) rotate([90,0,0]) cylinder(d=d, h=width, center=true, $fn=64);
}

module frame() {
    z = ground_clearance;
    beam_x(50, -frame_width/2, z, frame_length-100);
    beam_x(50, frame_width/2-main_tube, z, frame_length-100);
    for (x=[100, 450, 800, 1150, 1450])
        beam_y(x, -frame_width/2, z, frame_width);
    beam_y(0, -425, z, 850);
    beam_y(frame_length-main_tube, -425, z, 850);

    // seat rails
    beam_x(520, -170, z+main_tube, 520, secondary_tube);
    beam_x(520, 145, z+main_tube, 520, secondary_tube);
    // pedal rails
    beam_x(120, -130, z+main_tube, 450, secondary_tube);
    beam_x(120, 105, z+main_tube, 450, secondary_tube);
    // side rails
    beam_x(350, -frame_width/2-25, z+120, 800, secondary_tube);
    beam_x(350, frame_width/2, z+120, 800, secondary_tube);
}

module placeholders() {
    // seat
    color("blue") translate([600,-210,100]) cube([450,420,80]);
    color("blue") translate([900,-210,180]) rotate([0,-15,0]) cube([60,420,500]);
    // battery centred behind seat
    color("green") translate([1070,-170,100]) cube([300,340,180]);
    // motor at right rear
    color("orange") translate([1180,220,110]) cube([250,180,180]);
    // controller at left rear
    color("red") translate([1180,-370,120]) cube([220,130,70]);
}

module running_gear() {
    front_x = 250;
    rear_x = front_x + wheelbase;
    zf = front_wheel_d/2;
    zr = rear_wheel_d/2;
    color("black") wheel(front_x, -front_track/2, zf, front_wheel_d, wheel_width);
    color("black") wheel(front_x, front_track/2, zf, front_wheel_d, wheel_width);
    color("black") wheel(rear_x, -rear_track/2, zr, rear_wheel_d, wheel_width);
    color("black") wheel(rear_x, rear_track/2, zr, rear_wheel_d, wheel_width);
    color("silver") translate([rear_x,0,zr]) rotate([90,0,0]) cylinder(d=30,h=rear_track+120,center=true,$fn=32);
}

frame();
placeholders();
running_gear();
