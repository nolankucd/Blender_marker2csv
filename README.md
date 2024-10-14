# Blender_marker2csv

Some simple scripts to extract tracker data from Blender. Run these scripts in Blender's scripting text editor (via the scripting workspace for example) to write data from tracking markers you have applied to a video to a CSV file.

## marker2csv.py
Converts a tracker coordinates from video to a CSV file.
This only provides the (x,y) coordinates of each tracker in the format and is the simplest way to get what you may need.
| marker_name	time (s) |	location_x | location_y |

<img width="600" alt="image" src="https://github.com/user-attachments/assets/02c0ecd1-2457-4bbb-8838-efccfc66b101">

## marker_corners2csv.py

If you also want to get the rotation and scale of your trackers this script writes out the corners of each tracker in the follwoing format.
Then you can use this to determine the rotation and scale of the tracking box.

| marker_name	time (s) |	corner_1_x |	corner_1_y |	corner_2_x |	corner_2_y |	corner_3_x |	corner_3_y |	corner_4_x |	corner_4_y |

https://github.com/user-attachments/assets/349ad3c1-2887-451f-b007-5a7bcc47448e

