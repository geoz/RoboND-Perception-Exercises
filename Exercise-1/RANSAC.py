# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')


# TODO: Voxel Grid Downsampling
# Decrease resolution for faster calculations, but it should still do 
# a good job of representing the point cloud as a whole.
# Create a VoxelGrid filter object for our input point cloud
vox = cloud.make_voxel_grid_filter()
# Choose a voxel (also known as leaf) size
# Note: this (1) is a poor choice of leaf size   
# Experiment and find the appropriate size!
LEAF_SIZE = 0.01
# Set the voxel (or leaf) size  
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)
# Call the filter function to obtain the resultant downsampled point cloud
cloud_filtered = vox.filter()
# Call the filter function to obtain the resultant downsampled point cloud
filename = 'voxel_downsampled.pcd'
pcl.save(cloud_filtered, filename)

# TODO: PassThrough Filter
# If you have some prior information about the location of your target
# in the scene,you can apply a Pass Through Filter to remove useless data
# from your point cloud.
# The Pass Through Filter works much like a cropping tool, which allows you 
# to crop any given 3D point cloud by specifying an axis with 
# cut-off values along that axis.
# Create a PassThrough filter object:
passthrough = cloud_filtered.make_passthrough_filter()
# Assign axis and range to the passthrough filter object.
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
axis_min = 0.76
axis_max = 1.1
passthrough.set_filter_limits(axis_min, axis_max)
# Finally use the filter function to obtain the resultant point cloud. 
cloud_filtered = passthrough.filter()
filename = 'pass_through_filtered.pcd'
pcl.save(cloud_filtered, filename)

# TODO: RANSAC Plane Segmentation
# Create the segmentation object
seg = cloud_filtered.make_segmenter()
# Set the model you wish to fit 
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)
# Max distance for a point to be considered fitting the model
# Experiment with different values for max_distance 
# for segmenting the table
max_distance = 0.01
seg.set_distance_threshold(max_distance)
# Call the segment function to obtain set of inlier indices and model coefficients
inliers, coefficients = seg.segment()


# Extract inliers
# TODO: Extract inliers and outliers
extracted_inliers = cloud_filtered.extract(inliers, negative=False)


# Save pcd for table
# pcl.save(cloud, filename)
filename = 'extracted_inliers.pcd'
pcl.save(extracted_inliers, filename)


# Extract outliers


# Save pcd for tabletop objects


