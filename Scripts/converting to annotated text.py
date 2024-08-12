import sqlite3

def extract_tracking_data(sqlite_path, output_txt_path):
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    cursor.execute("SELECT frame_number, trajectory_id, x_coordinate, y_coordinate FROM positions")

    with open(output_txt_path, 'w') as f:
        for row in cursor.fetchall():
            frame_number, trajectory_id, x_coordinate, y_coordinate = row
            bb_left, bb_top, bb_width, bb_height, conf = 0, 0, 0, 0, 1
            f.write(f"{frame_number},{trajectory_id},{bb_left},{bb_top},{bb_width},{bb_height},{conf},{x_coordinate},{y_coordinate},-1\n")

    conn.close()

# Example usage
sqlite_path = '/content/traffic-intelligence/scripts/default_database-bb.sqlite'
output_txt_path = '/content/tracker.txt'
extract_tracking_data(sqlite_path, output_txt_path)
