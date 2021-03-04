### mesh2keypoint.py
- assumptions
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
    - load mesh2keypoint_util.py with mesh, dataset, camera
    - get and dump the result to the output directory
### mesh2keypoint_util.py
- init(mesh, dataset, camera)
    - load smpl and mano regressor # don't want to do this everytime
    - self.mesh
    - self.keypoint
    - self.depthmap
    - self.contour
- load_mesh(mesh)
    - self.keypoint = self.depthmap = self.contour = None
    - return mesh
- get_keypoint()
- get_depthmap()
- get_contour()