import numpy as np

class Object3D:
    def __init__(self, vertices):
        # vertices is expected to be a numpy array of shape (n, 3) where n is the number of vertices
        self.vertices = vertices

    def scale_to_unit(self):
        # Calculate the bounding box of the object
        min_bound = np.min(self.vertices, axis=0)
        max_bound = np.max(self.vertices, axis=0)
        
        # Calculate the dimensions of the bounding box
        dimensions = max_bound - min_bound
        
        # Find the maximum dimension
        max_dimension = np.max(dimensions)
        
        # Calculate the scale factor to make the max dimension equal to 1
        scale_factor = 1 / max_dimension
        
        # Apply the scale factor to all vertices
        self.vertices *= scale_factor

        # Optionally, translate the object to center it around the origin
        center = (max_bound + min_bound) / 2
        self.vertices -= center * scale_factor

    @staticmethod
    def load_obj(file_path):
        vertices = []
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    # Parse vertex line
                    _, x, y, z = line.strip().split()
                    vertices.append([float(x), float(y), float(z)])
        return Object3D(np.array(vertices))

    def save_obj(self, file_path):
        with open(file_path, 'w') as file:
            # Write vertices
            for vertex in self.vertices:
                file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")

# Example usage
input_path = 'input.obj'
output_path = 'scaled_output.obj'

# Load the object
object3d = Object3D.load_obj(input_path)

# Scale the object to a unit of 1
object3d.scale_to_unit()

# Save the scaled object
object3d.save_obj(output_path)

print(f"Scaled object saved to {output_path}")
