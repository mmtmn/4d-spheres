import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

# The values ​​related to each point. This can be a "Dataframe pandas" 
# for example where each column is linked to a variable <-> 1 dimension. 
# The idea is that each line = 1 pt in 4D.
do_random_pt_example = True;

index_x = 0; index_y = 1; index_z = 2; index_c = 3;
list_name_variables = ['x', 'y', 'z', 'c'];
name_color_map = 'seismic';

if do_random_pt_example:
    number_of_points = 200;
    x = np.random.rand(number_of_points);
    y = np.random.rand(number_of_points);
    z = np.random.rand(number_of_points);
    c = np.random.rand(number_of_points);
else:
    # Example where we have a "Pandas Dataframe" where each line = 1 pt in 4D.
    # We assume here that the "data frame" "df" has already been loaded before.
    x = df[list_name_variables[index_x]]; 
    y = df[list_name_variables[index_y]]; 
    z = df[list_name_variables[index_z]]; 
    c = df[list_name_variables[index_c]];
name_color_map_surface = 'Greens';  # Colormap for the 3D surface only.

fig = plt.figure(); 
ax = fig.add_subplot(111, projection='3d');
ax.set_xlabel(list_name_variables[index_x]); ax.set_ylabel(list_name_variables[index_y]);
ax.set_zlabel(list_name_variables[index_z]);
plt.title('%s in fcn of %s, %s and %s' % (list_name_variables[index_c], list_name_variables[index_x], list_name_variables[index_y], list_name_variables[index_z]) );

# In this case, we will have 2 color bars: one for the surface and another for 
# the "scatter plot".
# For example, we can place the second color bar under or to the left of the figure.
choice_pos_colorbar = 2;

#The scatter plot.
img = ax.scatter(x, y, z, c = c, cmap = name_color_map);
cbar = fig.colorbar(img, shrink=0.5, aspect=5); # Default location is at the 'right' of the figure.
cbar.ax.get_yaxis().labelpad = 15; cbar.ax.set_ylabel(list_name_variables[index_c], rotation = 270);

# The 3D surface that serves only to connect the points to help visualize 
# the distances that separates them.
# The "alpha" is used to have some transparency in the surface.
surf = ax.plot_trisurf(x, y, z, cmap = name_color_map_surface, linewidth = 0.2, alpha = 0.25);

# The second color bar will be placed at the left of the figure.
if choice_pos_colorbar == 1: 
    #I am trying here to have the two color bars with the same size even if it 
    #is currently set manually.
    cbaxes = fig.add_axes([1-0.78375-0.1, 0.3025, 0.0393823, 0.385]);  # Case without tigh layout.
    #cbaxes = fig.add_axes([1-0.844805-0.1, 0.25942, 0.0492187, 0.481161]); # Case with tigh layout.

    cbar = plt.colorbar(surf, cax = cbaxes, shrink=0.5, aspect=5);
    cbar.ax.get_yaxis().labelpad = 15; cbar.ax.set_ylabel(list_name_variables[index_z], rotation = 90);

# The second color bar will be placed under the figure.
elif choice_pos_colorbar == 2: 
    cbar = fig.colorbar(surf, shrink=0.75, aspect=20,pad = 0.05, orientation = 'horizontal');
    cbar.ax.get_yaxis().labelpad = 15; cbar.ax.set_xlabel(list_name_variables[index_z], rotation = 0);
#end
plt.show();