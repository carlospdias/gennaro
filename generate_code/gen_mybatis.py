from jinja2 import Environment, FileSystemLoader

class GenMyBatis(object):

    def __init__(self, json_data):
        self.json_data_seed = json_data
        file_loader = FileSystemLoader('templates')
        self.env = Environment(loader=file_loader)
        
  

    def prepare_mappers(self):
        template = self.env.get_template('objetoMapper.txt')
        objetos  = self.json_data_seed['modelos']["java"]
        for obj in objetos:
            print(template.render(objeto=obj))
           
      
    
