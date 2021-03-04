import torch
import numpy as np
import os
import argparse
import json

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--mesh', default=None, help='Path to mesh directory')
parser.add_argument('--joint_regressor', default=None, help='Path to MANO or SMPL joint regressor')
parser.add_argument('--camera', default=None, help='Path to camera view file')
parser.add_argument('--write_contour', default=None, help='Path to write contour')
parser.add_argument('--wite_depthmap', default=None, help='Path to write depth map')
parser.add_argument('--write_keypoint', default=None, help='Path to write 3D keypoint')
parser.add_argument('--write_all', default=None, help='path to write contour, depth map, and 3D keypoint')

