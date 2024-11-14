import numpy as np

def center_vertices(vertices):
    # Calculate the centroid of the vertices
    centroid = np.mean(vertices, axis=0)
    
    # Center the vertices by subtracting the centroid
    centered_vertices = vertices - centroid
    
    return centered_vertices

# Example usage
vertices = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    # ... other vertices
])

centered_vertices = center_vertices(vertices)
print("Centered vertices:\n", centered_vertices)
