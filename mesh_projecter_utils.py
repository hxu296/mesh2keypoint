import numpy as np
from camera_utils import world_to_camera
from
class ProjectMesh:

    def __init__(self, mesh, camera, joint_regressor):
        self.mesh = mesh                        # numpy array of shape (frame_count, 6980, 3)
        self.joint_regressor = joint_regressor  # either 'mano' or 'smpl'
        self.camera = camera                    # {'t': translation, 'R': rotation}

    def get_keypoint(self):
        world_keypoint = np.dot(self.joint_regressor, self.mesh)
        camera_keypoint = world_to_camera(world_keypoint, self.camera['R'], self.camera['t'])
        return camera_keypoint

    def get_depthmap(self):

        return None

    def get_contour(self):
        return None

