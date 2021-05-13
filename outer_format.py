import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString


class FileDump(ABC):

    @abstractmethod
    def write(self, filepath, data):
        pass


class JSONDump(FileDump):

    def write(self, filepath, data):
        with open(filepath, 'tw', encoding='UTF-8') as file:
            return json.dump(data, file, sort_keys=True, indent=2)


class XMLDump(FileDump):

    def write(self, filepath, data):

        rooms = ET.Element('rooms')

        for i in range(len(data)):

            room = ET.SubElement(rooms, 'item')

            room_id = ET.SubElement(room, 'id')
            room_id.text = str(data[i]["id"])

            room_name = ET.SubElement(room, 'name')
            room_name.text = str(data[i]["name"])

            students = ET.SubElement(room, 'students')

            for student in range(len(data[i]["students"])):
                stud = ET.SubElement(students, 'item')

                stud_id = ET.SubElement(stud, 'id')
                stud_id.text = str(data[i]["students"][student]["id"])

                stud_name = ET.SubElement(stud, 'name')
                stud_name.text = str(data[i]["students"][student]["name"])

                stud_room = ET.SubElement(stud, 'room')
                stud_room.text = str(data[i]["students"][student]["room"])

        tree = ET.tostring(rooms, encoding='unicode')

        with open('outer_format_files/rooms_sorted.xml', 'w') as file:
            file.write(parseString(tree).toprettyxml())
