import bpy
import csv

# Access the MovieClip
clip = bpy.data.movieclips[0]

# The path of your output CSV file
output_filepath = "/Users/$USERNAME/Desktop/"
output_filename = clip.name+ \
                    "_"+str(bpy.data.scenes[0].frame_start)+ \
                    "_"+str(bpy.data.scenes[0].frame_end)+".csv"

# Access its tracking data
tracking_data = clip.tracking

with open(output_filepath+output_filename, 'w', newline='') as csvfile:
    fieldnames = ['marker_name', 'time (s)', 'location_x', 'location_y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for object in tracking_data.objects:
        for track in object.tracks:
            for marker in track.markers:
                writer.writerow({'marker_name': track.name,
                                'time (s)': (marker.frame - bpy.data.scenes[0].frame_start + 1)/clip.fps, 
                                'location_x': marker.co.xy[0], 'location_y': marker.co.xy[1]})
