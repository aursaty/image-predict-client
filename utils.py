import json
import csv


def save_image(content):
    """Save image from bytes to the file
    """
    with open('output.jpg', 'wb') as f:
        f.write(content)


def extract_and_store_predictions(data, filename='output.csv'):
    """Extract prediction classes information: class name, confidence, box placement on the image, store to the csv.

    Args:
        data: json response from ultralytics model
        filename: file where to store the outputs
    """
    data_file = open(filename, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for row in data:
        if count == 0:
            header = list(row.keys())
            header_without_box = header[0:-1]
            header_box = ['x1','y1','x2','y2']
            header_without_box += header_box
            header = header_without_box
            csv_writer.writerow(header)
        count += 1
        if len(row) > 1:
            sheetsRow = list(row.values())[0:-1]
            box_data = list(row.values())[-1]
            sheetsRow.extend(list((box_data).values()))
            csv_writer.writerow(sheetsRow)
    data_file.close()
