### sample_kp.py
- assumption
    - input mesh
      - file type: .npy
      - array shape: frame_index * 6980 * 3
    - input camera view
      - file type .json
      - dictionary (k,v) pairs: {"T":translation_matrix, "R":rotation_matrix}
- what this file does
    - pre-process command line args
      - assert mesh and camera, and output directory exist
      - assert dataset is either smpl or mano
    - load and pre-process mesh and camera
      - cast mesh into a numpy array of shape (frame_count * 6980 * 3)
        - if multiple meshes in the directory, iteratively load-process-dump each mesh to save memory 
    - load samle_kp_util.py with mesh, dataset, camera
    - get and dump the result to the output directory
- flag
   - path_to_config

### config.yaml
- path_to_mesh [path to mesh directory or file] 
- path_to_regressor [mano or smpl regressor] 
- path_to_camera [path to camera view file] 
- write_contour [path to write contour] 
- write_depthmap [path to write depth map] 
- write_2d_keypoint [path to write keypoint] 
- write_all [path to write contour, depthmap, and keypoint]
- device [cpu or gpu]

### sample_kp_utils.py (core function)
- initialized with a mesh, a camera (rotation and translation matrix), and a joint regressor (smpl or mano)
- get_3d_keypoint
- get_2d_keypoint
- get_depthmap
    - based on AMASS_unify's implementation in depth.py using vispy
- get_contour
    - differentiate human mesh and background

### camera_utils.py (implementation from Facebook)
- qrot (rotate based on quaternion)
- qinverse
- wrap (torch to numpy without loss of generality)
- world_to_camera (receive rotation & translation matrix)
- camera_to_world
- project_to_2d (receive camera intrinsics)
- project_to_2d_linear (use only focal length and principal point)

