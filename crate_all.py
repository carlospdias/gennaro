import json
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

def create_tela_jsp(json_data):
    template = env.get_template('tela_jsp.txt')
    output = template.render(persons=json_data["mapper"]["attributes"])
    print(output)
    #for att in json_data['mapper']['attributes']:
    #    print(att['java_name'])

def create_request_object(json_data):
    template = env.get_template('request.txt')
    output = template.render(persons=json_data["mapper"]["attributes"], _object=json_data["mapper"]["_object"])
    print(output)
    #for att in json_data['mapper']['attributes']:
    #    print(att['java_name'])

def create_controller(json_data):
    template = env.get_template('controller.txt')
    output = template.render(atributos=json_data["mapper"])
    print(output)

def create_dao():
    return "dao"

def create_usecase():
    return "usecase"


def get_data():
    with open('res.json', mode='r', buffering=1024, encoding="UTF-8" ) as jr:
        json_data = json.loads(jr.read())
        #create_tela_jsp(json_data)
        #create_request_object(json_data)
        create_controller(json_data)


get_data()
