import bpy
import csv
from pathlib import Path

# Access the MovieClip
clip = bpy.data.movieclips[0]

# Get the user's Desktop folder in an OS-agnostic way
desktop = Path.home() / "Desktop"

# Fallback: if no Desktop exists, use the home directory
if not desktop.exists():
    desktop = Path.home()

# Build the output filename
output_filename = (
    f"{clip.name}_{bpy.data.scenes[0].frame_start}_{bpy.data.scenes[0].frame_end}.csv"
)

output_filepath = desktop / output_filename

# Access its tracking data
tracking_data = clip.tracking

with open(output_filepath, 'w', newline='') as csvfile:
    fieldnames = ['marker_name', 'time (s)', 'location_x', 'location_y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for obj in tracking_data.objects:
        for track in obj.tracks:
            for marker in track.markers:
                writer.writerow({
                    'marker_name': track.name,
                    'time (s)': (marker.frame - bpy.data.scenes[0].frame_start + 1) / clip.fps,
                    'location_x': marker.co.xy[0],
                    'location_y': marker.co.xy[1],
                })

print(f"CSV saved to: {output_filepath}")
