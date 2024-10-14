# Blender_marker2csv

Some simple scripts to extract tracker data from Blender

## marker2csv.py
Converts Blender's tracker coordinates from video to a CSV file.
This only provides the (x,y) coordinates of each tracker in the format
| marker_name	time (s) |	location_x | location_y |

<img width="600" alt="image" src="https://github.com/user-attachments/assets/02c0ecd1-2457-4bbb-8838-efccfc66b101">

## marker_corners2csv.py

Run this script in Blender to write the tracking markers in a video to a CSV file.

| marker_name	time (s) |	corner_1_x |	corner_1_y |	corner_2_x |	corner_2_y |	corner_3_x |	corner_3_y |	corner_4_x |	corner_4_y |

https://github.com/user-attachments/assets/349ad3c1-2887-451f-b007-5a7bcc47448e

