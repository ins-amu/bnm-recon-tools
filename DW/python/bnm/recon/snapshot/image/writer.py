# -*- coding: utf-8 -*-
import os

import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import proj3d
import numpy

class ImageWriter(object):
    snapshot_extension = ".png"
    snapshots_directory = None

    def __init__(self):
        snapshot_directory = os.environ['FIGS']

        if snapshot_directory is not None:

            if not os.path.exists(snapshot_directory):
                os.mkdir(snapshot_directory)

            self.snapshots_directory = snapshot_directory


    def get_path(self, result_name):
        return self.snapshots_directory + '/' + result_name + self.snapshot_extension


    def write_matrix(self, matrix, result_name):
        pyplot.imshow(matrix, cmap="gray")
        pyplot.axis('off')
        pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)


    def write_2_matrices(self, matrix_background, matrix_overlap, result_name):
        pyplot.imshow(matrix_background, cmap="gray")
        pyplot.imshow(matrix_overlap, cmap="hot", alpha=0.3)
        pyplot.axis('off')
        pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)


    def write_3_matrices(self, matrix_background, matrix_overlap_1, matrix_overlap_2, result_name):
        pyplot.imshow(matrix_background, cmap="gray")
        pyplot.imshow(matrix_overlap_1, cmap="hot", alpha=0.3)
        pyplot.imshow(matrix_overlap_2, cmap="jet", alpha=0.5)
        pyplot.axis('off')
        pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)


    def write_surface(self, surface, result_name, positions=[(0, 0),(0, 90), (0, 180), (0, 270), (90, 0), (270, 0)]):
        x = surface.vertices[:, 0]
        y = surface.vertices[:, 1]
        z = surface.vertices[:, 2]

        fig=pyplot.figure()

        ax = fig.gca(projection='3d')
        ax.set_xlim3d(-120, 60)
        ax.set_ylim3d(-120, 120)
        ax.set_zlim3d(-60, 120)
        ax.dist = 3

        ax.plot_trisurf(x, y, z, triangles=surface.triangles, color='g', linewidth=0.4)
        pyplot.axis('off')

        snapshot_index = 0
        for e, a in positions:
            ax.view_init(elev=e, azim=a)
            pyplot.savefig(self.get_path(result_name + str(snapshot_index)))
            snapshot_index = snapshot_index + 1


    def write_surface_with_annotation(self, surface, annot, result_name, positions=[(0, 0),(0, 90), (0, 180), (0, 270), (90, 0), (270, 0)]):
        x = surface.vertices[:, 0]
        y = surface.vertices[:, 1]
        z = surface.vertices[:, 2]

        fig=pyplot.figure()

        ax=fig.gca(projection='3d')
        ax.set_xlim3d(-120, 60)
        ax.set_ylim3d(-120, 120)
        ax.set_zlim3d(-60, 120)
        ax.dist = 4

        face_colors = annot.face_colors(surface.triangles)

        normals = surface.compute_normals()
        face_colors = ax._shade_colors(face_colors, normals)

        poly_line = ax.plot_trisurf(x, y, z, triangles=surface.triangles)
        poly_line.set_edgecolor(face_colors)
        poly_line.set_facecolor(face_colors)

        pyplot.axis('off')

        snapshot_index = 0
        for e, a in positions:
            ax.view_init(elev=e, azim=a)
            pyplot.savefig(self.get_path(result_name + str(snapshot_index)))
            snapshot_index = snapshot_index + 1


    def write_matrix_and_surface(self, X,Y,matrix_background, surface_x_array, surface_y_array, clear_flag): #, result_name):
        if clear_flag == True:
            pyplot.clf()
        #pyplot.imshow(matrix_background, cmap="gray")
        pyplot.pcolormesh(X, Y, numpy.array(matrix_background),cmap="gray")
        #ax.set_aspect('equal')
        for s in range(0, len(surface_x_array)):
            pyplot.plot(surface_x_array[s][:], surface_y_array[s][:], 'y')
        # pyplot.axis('off')
        # pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)


    def save_figure(self, result_name):
        pyplot.axis('off')
        pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)


    def write_matrix_and_surfaces(self, matrix_background, surf1_x_array, surf1_y_array, clear_flag, surf): #, result_name):
        if clear_flag == True:
            pyplot.clf()
        if surf == 'pial':
            contour_color = 'r'
        else:
            contour_color = 'y'
        pyplot.imshow(matrix_background, cmap="gray")
        for s in range(0, len(surf1_x_array)):
            pyplot.plot(surf1_x_array[s][:], surf1_y_array[s][:], contour_color)
        # pyplot.axis('off')
        # pyplot.savefig(self.get_path(result_name), bbox_inches='tight', pad_inches=0.0)