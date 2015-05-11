#!/usr/bin/env python

# external
from pydy.viz.shapes import Cylinder, Sphere
from pydy.viz.scene import Scene
from pydy.viz.visualization_frame import VisualizationFrame

# local
from derive import I, O, links, particles, q, u
from simulate import param_syms, state_trajectories, param_vals
from simulate import link_length, link_radius, particle_radius

# A cylinder will be attached to each link and a sphere to each bob for the
# visualization.

viz_frames = []

for i, (link, particle) in enumerate(zip(links, particles)):

    link_shape = Cylinder(name='cylinder{}'.format(i),
                          radius=link_radius,
                          length=link_length,
                          color='red')

    viz_frames.append(VisualizationFrame('link_frame{}'.format(i), link,
                                         link_shape))

    particle_shape = Sphere(name='sphere{}'.format(i),
                            radius=particle_radius,
                            color='blue')

    viz_frames.append(VisualizationFrame('particle_frame{}'.format(i),
                                         link.frame,
                                         particle,
                                         particle_shape))

# Now the visualization frames can be passed in to create a scene.
scene = Scene(I, O, *viz_frames)

# And the motion of the shapes is generated by providing the scene with the
# state trajectories.
print('Generating transform time histories.')
scene.generate_visualization_json(q + u, param_syms, state_trajectories,
                                  param_vals)
print('Done.')
scene.display()
