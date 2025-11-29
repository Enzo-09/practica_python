"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 """


import os 
import xml.etree.cElementTree as xml
import json

data = {
    "name": "enzo",
    "age": 25,
    "birth_date": "09-08-2004",
    "lenguajes": "[python, typescript, react]"
}

xml_file = "Enzo-09.xml"
json_file = "Enzo-09.json"

def create_xml():

    root = xml.Element("programador")
    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item") == item
        else:
            child.text = str(value)
    tree = xml.ElementTree(root)
    tree.write(xml_file)
create_xml()


def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()

with open (json_file, "r") as json_data:
    print(json_data.read())



"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
#extra
class data:
    def __init__(self, name, age, birth_date, lenguajes):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.lenguajes = lenguajes

with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    lenguajes = []
    for item in root.find("lenguajes"):
        lenguajes.append(item.text)
    xml_class = data(name, age, birth_date, lenguajes)
    print (xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["lenguajes"]
        )
    print(json_class.__dict__)
os.remove(xml_file)
os.remove(json_file)




    