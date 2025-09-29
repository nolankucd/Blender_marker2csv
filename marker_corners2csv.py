import bpy
import csv
from pathlib import Path

# Access the MovieClip
clip = bpy.data.movieclips[0]

# Resolve the user's Desktop folder (cross-platform)
desktop = Path.home() / "Desktop"
if not desktop.exists():
    desktop = Path.home()  # fallback to home directory if no Desktop

# Build the output filename
output_filename = (
    f"{clip.name}_{bpy.data.scenes[0].frame_start}_{bpy.data.scenes[0].frame_end}.csv"
)
output_filepath = desktop / output_filename

# Access tracking data
tracking_data = clip.tracking

with open(output_filepath, 'w', newline='') as csvfile:
    # Defining columns: marker name, time, and the four corner coordinates of the pattern
    fieldnames = [
        'marker_name', 'time (s)',
        'corner_1_x', 'corner_1_y',
        'corner_2_x', 'corner_2_y',
        'corner_3_x', 'corner_3_y',
        'corner_4_x', 'corner_4_y'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for obj in tracking_data.objects:
        for track in obj.tracks:
            for marker in track.markers:
                corners = marker.pattern_corners  # list of 4 (x, y) pairs
                writer.writerow({
                    'marker_name': track.name,
                    'time (s)': (marker.frame - bpy.data.scenes[0].frame_start + 1) / clip.fps,
                    'corner_1_x': corners[0][0], 'corner_1_y': corners[0][1],
                    'corner_2_x': corners[1][0], 'corner_2_y': corners[1][1],
                    'corner_3_x': corners[2][0], 'corner_3_y': corners[2][1],
                    'corner_4_x': corners[3][0], 'corner_4_y': corners[3][1],
                })

print(f"CSV saved to: {output_filepath}")
