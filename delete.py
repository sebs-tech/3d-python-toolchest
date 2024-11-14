import numpy as np

def extract_vertices_from_obj(file_path):
    vertices = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                # Extract vertex positions from lines starting with 'v '
                _, x, y, z = line.strip().split()
                vertices.append([float(x), float(y), float(z)])
    
    # Convert the list of vertices to a NumPy array
    vertices_array = np.array(vertices)
    return vertices_array

# Example usage
input_path = 'input.obj'
vertices_array = extract_vertices_from_obj(input_path)
print("Vertices array:\n", vertices_array)
