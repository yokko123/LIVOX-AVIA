import open3d as o3d
import numpy as np
import math

# Read the PCD file
pt_cloud = o3d.io.read_point_cloud("data/10.pcd")

# Read the bounding box coordinates from the text file
bounding_boxes = []
with open("data/10.txt", "r") as file:
    for line in file:
        values = list(map(float, line.split(',')))
        bounding_boxes.append(values)
# print(bounding_boxes[2])
# Visualize the point cloud
# o3d.visualization.draw_geometries([pt_cloud])

# Create lines representing the bounding boxes
line_sets = []
for bbox in bounding_boxes:
    xctr, yctr, zctr, xlen, ylen, zlen, _, _, zrot = bbox
    # Define the 8 corner points of the bounding box
    corners = np.array([
        [-xlen/2, -ylen/2, -zlen/2],
        [xlen/2, -ylen/2, -zlen/2],
        [xlen/2, ylen/2, -zlen/2],
        [-xlen/2, ylen/2, -zlen/2],
        [-xlen/2, -ylen/2, zlen/2],
        [xlen/2, -ylen/2, zlen/2],
        [xlen/2, ylen/2, zlen/2],
        [-xlen/2, ylen/2, zlen/2]
    ])

    # Apply rotation to the bounding box around the Z-axis
    zrot = zrot*(math.pi/180) #converting degree to radian 
    rot_z = np.array([[math.cos(zrot), -math.sin(zrot), 0], [math.sin(zrot), math.cos(zrot), 0], [0, 0, 1]])
    corners = np.dot(corners, rot_z.T)

    # Translate the corners to the center of the bounding box
    corners = corners + np.array([xctr, yctr, zctr])

    # Define the edges of the bounding box
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    # Create a line set for the bounding box
    line_set = o3d.geometry.LineSet()
    line_set.points = o3d.utility.Vector3dVector(corners)
    line_set.lines = o3d.utility.Vector2iVector(edges)
    line_sets.append(line_set)

# Visualize the point cloud with the bounding boxes
o3d.visualization.draw_geometries([pt_cloud] + line_sets)
