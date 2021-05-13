import json
import argparse
from outer_format import JSONDump, XMLDump
from time import time


def arg_parser():
    parser = argparse.ArgumentParser(description='With this script, you can combine two files into a file of the '
                                                 'desired format')
    parser.add_argument('students_file_path', type=str, help='Provide a path to students file')
    parser.add_argument('rooms_file_path', type=str, help='Provide a path to rooms file')
    parser.add_argument('outer_format', type=str, help='Choose an outer format')

    return parser


def union_data(students, rooms):
    rooms_sorted = [{'id': rooms[i]['id'], 'name': rooms[i]['name'], 'students': []} for i in range(len(rooms))]

    for i in range(len(students)):
        rooms_sorted[students[i]['room']]['students'].append({
            "id": students[i]['id'],
            "name": students[i]['name'],
            "room": students[i]['room']
        })

    return rooms_sorted


def main(students_path, rooms_path, file_format):
    try:
        with open(students_path) as file_with_studs:
            students = json.load(file_with_studs)
        with open(rooms_path) as file_with_rooms:
            rooms = json.load(file_with_rooms)
    except FileNotFoundError as error:
        print(f'{error.filename} was not found')
        return None

    data = union_data(students, rooms)

    if file_format == 'json':
        JSONDump.write(JSONDump, 'outer_format_files/rooms_sorted.json', data)
    elif file_format == 'xml':
        XMLDump.write(XMLDump, 'outer_format_files/rooms_sorted.xml', data)
    else:
        raise argparse.ArgumentTypeError('Value has to be json or xml')


if __name__ == '__main__':
    sec = time()
    args = arg_parser().parse_args()
    main(args.students_file_path, args.rooms_file_path, args.outer_format)
    print(time() - sec)
