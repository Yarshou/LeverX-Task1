import argparse
from outer_format import JSONDump, XMLDump
from file_loader import JSONLoad


def arg_parser():
    parser = argparse.ArgumentParser(description='With this script, you can combine two files into a file of the '
                                                 'desired format')
    parser.add_argument('students_file_path', type=str, help='Provide a path to students file')
    parser.add_argument('rooms_file_path', type=str, help='Provide a path to rooms file')
    parser.add_argument('outer_format', type=str, help='Choose an outer format', choices=['xml', 'json'])

    return parser


def union_data(students, rooms):
    rooms_sorted = [{'id': rooms[i]['id'], 'name': rooms[i]['name'], 'students': []} for i in range(len(rooms))]

    for student in students:
        rooms_sorted[student['room']]['students'].append({
            "id": student['id'],
            "name": student['name'],
            "room": student['room']
        })

    return rooms_sorted


def main(students_path, rooms_path, file_format):
    loader = JSONLoad()

    try:
        students = loader.load(students_path)
    except FileNotFoundError as error:
        print(f'{error.filename} was not found')
        return None

    try:
        rooms = loader.load(rooms_path)
    except FileNotFoundError as error:
        print(f'{error.filename} was not found')
        return None

    data = union_data(students, rooms)

    if file_format == 'json':
        with open('outer_format_files/rooms_sorted.json', 'tw+', encoding='UTF-8') as file:
            JSONDumper = JSONDump()
            file.write(JSONDumper.dump(data))

    elif file_format == 'xml':
        with open('outer_format_files/rooms_sorted.xml', 'w+') as file:
            XMLDumper = XMLDump()
            file.write(XMLDumper.dump(data))


if __name__ == '__main__':
    args = arg_parser().parse_args()
    main(args.students_file_path, args.rooms_file_path, args.outer_format)
