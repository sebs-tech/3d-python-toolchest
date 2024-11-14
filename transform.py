import numpy as np
from scipy.spatial.transform import Rotation as R

class Transform3D:
    def __init__(self, vertices):
        # vertices is expected to be a numpy array of shape (n, 3) where n is the number of vertices
        self.vertices = vertices

    def apply_transform(self, origin, translation, quaternion, scale):
        # 1. Translate vertices to the origin for rotation and scaling
        transformed_vertices = self.vertices - origin

        # 2. Apply scaling
        transformed_vertices *= scale

        # 3. Apply rotation using quaternion
        rotation = R.from_quat(quaternion)  # quaternion format: [x, y, z, w]
        transformed_vertices = rotation.apply(transformed_vertices)

        # 4. Apply translation
        transformed_vertices += translation + origin

        return transformed_vertices

# Example usage
vertices = np.array([
    [1.0, 1.0, 1.0],
    [2.0, 2.0, 2.0],
    [3.0, 3.0, 3.0],
    # ... other vertices
])

# User-defined transformation parameters
origin = np.array([0.0, 0.0, 0.0])        # Origin point for transformation
translation = np.array([1.0, 2.0, 3.0])    # Translation amount
quaternion = [0.0, 0.0, np.sin(np.pi / 4), np.cos(np.pi / 4)]  # 90 degrees rotation around Z-axis
scale = 2.0                                # Scaling factor

# Create Transform3D object and apply transformations
transform = Transform3D(vertices)
transformed_vertices = transform.apply_transform(origin, translation, quaternion, scale)

print("Transformed vertices:\n", transformed_vertices)
