from pyrobot import Robot

from os.path import dirname, join, abspath
from pyrep import PyRep
from pyrep.robots.mobiles.locobot import LoCoBot
from pyrep.robots.arms.locobot_arm import LoCoBotArm
from pyrep.robots.end_effectors.locobot_gripper import LoCoBotGripper
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy

common_config = {}
common_config['scene_path'] = join(dirname(abspath(__file__)), 'scene_locobot_stack_cube.ttt')


robot = Robot('vrep_locobot',common_config=common_config)
pos = [1,1, 3.14/2] #beware x, y is fliped!
robot.base.go_to_absolute(pos, smooth=False)