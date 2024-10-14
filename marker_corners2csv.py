import bpy
import csv

# Access the MovieClip
clip = bpy.data.movieclips[0]

# Output path for the CSV
output_filepath = "/Users/$USERNAME/Desktop/"
output_filename = clip.name + "_" + \
                    str(bpy.data.scenes[0].frame_start) + \
                    "_" + str(bpy.data.scenes[0].frame_end) + ".csv"

# Access tracking data
tracking_data = clip.tracking

with open(output_filepath + output_filename, 'w', newline='') as csvfile:
    # Defining columns: marker name, time, and the four corner coordinates of the pattern
    fieldnames = ['marker_name', 'time (s)',
                  'corner_1_x', 'corner_1_y',
                  'corner_2_x', 'corner_2_y',
                  'corner_3_x', 'corner_3_y',
                  'corner_4_x', 'corner_4_y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for obj in tracking_data.objects:
        for track in obj.tracks:
            for marker in track.markers:
                # Get pattern corner coordinates (4 corners)
                corner_1 = marker.pattern_corners[0]
                corner_2 = marker.pattern_corners[1]
                corner_3 = marker.pattern_corners[2]
                corner_4 = marker.pattern_corners[3]

                # Write to CSV
                writer.writerow({'marker_name': track.name,
                                 'time (s)': (marker.frame - bpy.data.scenes[0].frame_start + 1) / clip.fps,
                                 'corner_1_x': corner_1[0], 'corner_1_y': corner_1[1],
                                 'corner_2_x': corner_2[0], 'corner_2_y': corner_2[1],
                                 'corner_3_x': corner_3[0], 'corner_3_y': corner_3[1],
                                 'corner_4_x': corner_4[0], 'corner_4_y': corner_4[1]})
