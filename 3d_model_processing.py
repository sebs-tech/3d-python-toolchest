import open3d as o3d
import numpy as np
import trimesh


# Load the OBJ file
mesh = trimesh.load('src/3d_models/susanne/obj/susanne_tris.obj')

mesh_orig = trimesh.load('src/3d_models/susanne/obj/susanne_tris.obj')
# Print mesh information
print("Original: ", mesh)

# Translate Mesh
#translation_matrix = trimesh.transformations.translation_matrix([0, 0, 1])
#mesh.apply_transform(translation_matrix)

# 2. Rotation Matrix (Rotate 45 degrees around the Z-axis)
#rotation_matrix = trimesh.transformations.rotation_matrix(
#    angle=np.radians(45),  # 45 degree rotation
#    direction=[0, 0, 1],   # Rotation around Z-axis
#    point=mesh.centroid    # Rotate around the mesh's centroid
#)
#mesh.apply_transform(rotation_matrix)

# 3. Scaling Matrix (Scale the mesh uniformly)
scaling_matrix = trimesh.transformations.scale_matrix(factor=2.0, origin=mesh.centroid)
mesh.apply_transform(scaling_matrix)

translation_matrix = trimesh.transformations.translation_matrix([0, 5, 0])
mesh.apply_transform(translation_matrix)

# Randomized vertex colors
vertex_colors = (255,0,0,255)
mesh.visual.vertex_colors = vertex_colors

merged_meshes = trimesh.util.concatenate([mesh, mesh_orig])
print("Merged: ", merged_meshes)

# Export mesh
#merged_meshes.export('suzannes_merged.obj')
#mesh.export('suzanne_colored.obj')
mesh.show(viewer='gl')


