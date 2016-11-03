# -*- coding: utf-8 -*-

import argparse
import os
from bnm.recon.snapshot.image.processor import ImageProcessor


if __name__ == "__main__":

    arg_1vol = "1vol"
    arg_2vols = "2vols"
    arg_3vols = "3vols"
    arg_surf_annot = "surf_annot"
    arg_vol_surf = "vol_surf"
    arg_vol_white_pial = "vol_white_pial"

    parser = argparse.ArgumentParser(description="Generate a BNM snapshot")
    subparsers = parser.add_subparsers(title='Sub Commands', dest='subcommand')

    subcommand_1_vol = subparsers.add_parser(arg_1vol, help='Display a single volume')
    subcommand_2_vols = subparsers.add_parser(arg_2vols, help='Display 2 volumes overlapped')
    subcommand_3_vols = subparsers.add_parser(arg_3vols, help='Display 3 volumes overlapped')
    subcommand_surf_annot = subparsers.add_parser(arg_surf_annot, help='Display a surface with annotations')
    subcommand_vol_surf = subparsers.add_parser(arg_vol_surf, help='Display a surface overlapped on a volume')
    subcommand_vol_2surf = subparsers.add_parser(arg_vol_white_pial, help='Display white and pial surfaces over a volume')

    subcommand_1_vol.add_argument("volume")

    subcommand_2_vols.add_argument("background")
    subcommand_2_vols.add_argument("overlay")

    subcommand_3_vols.add_argument("background")
    subcommand_3_vols.add_argument("overlay1")
    subcommand_3_vols.add_argument("overlay2")

    subcommand_vol_surf.add_argument("background")
    subcommand_vol_surf.add_argument("surfaces_list", nargs='+')

    subcommand_surf_annot.add_argument("surface")
    subcommand_surf_annot.add_argument("annotation")

    subcommand_vol_2surf.add_argument("background")
    subcommand_vol_2surf.add_argument("-resampled_surface_name", default='')

    args = parser.parse_args()
    imageProcessor = ImageProcessor()
    if args.subcommand == arg_1vol:
        imageProcessor.show_single_volume(os.path.expandvars(args.volume))

    elif args.subcommand == arg_2vols:
        imageProcessor.overlap_2_volumes(os.path.expandvars(args.background), os.path.expandvars(args.overlay))

    elif args.subcommand == arg_3vols:
        imageProcessor.overlap_3_volumes(os.path.expandvars(args.background), os.path.expandvars(args.overlay1), os.path.expandvars(args.overlay2))

    elif args.subcommand == arg_surf_annot:
        imageProcessor.overlap_surface_annotation(os.path.expandvars(args.surface), os.path.expandvars(args.annotation))

    elif args.subcommand == arg_vol_surf:
        imageProcessor.overlap_volume_surface(os.path.expandvars(args.background), os.path.expandvars(args.surfaces_list))

    elif args.subcommand == arg_vol_white_pial:
        imageProcessor.overlap_volume_surfaces(os.path.expandvars(args.background), os.path.expandvars(args.resampled_surface_name))
