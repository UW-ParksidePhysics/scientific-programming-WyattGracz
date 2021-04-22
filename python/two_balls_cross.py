import vpython as vp

initial_position = vp.vector(-10., 10., 10.)
initial_velocity = vp.vector(2., -1., 2.)
ball = vp.sphere(pos=initial_position, radius=0.5, color=vp.color.red, make_trail=True)

initial_position2 = vp.vector(-6., 6., 6.)
initial_velocity2 = vp.vector(1., 1., 1.)
ball2 = vp.sphere(pos=initial_position, radius=0.5, color=vp.color.green, make_trail=True, trail_type = "points", trail_radius = 0.3, interval = 100, retain = 50)

animation_time_step = 0.1  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.1
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball.pos = vp.vector(x, y, z)

    vp.rate(rate_of_animation)
    x2 = initial_position2.x + initial_velocity2.x * time
    y2 = initial_position2.y + initial_velocity2.y * time
    z2 = initial_position2.z + initial_velocity2.z * time
    ball.pos = vp.vector(x, y, z)

    time += time_step
