from jinja2 import Environment, FileSystemLoader

class GenDao(object):

    def __init__(self, json_data):
        self.json_data_seed = json_data
        file_loader = FileSystemLoader('templates')
        self.env = Environment(loader=file_loader)
        
    def _prepare_daos_implementados(self, obj):
        template = self.env.get_template('objetoDaoMyBatis.txt')
        print(template.render(objeto=obj, pacote=obj['pacote']))

    def prepare_daos(self):
        template = self.env.get_template('objetoDao.txt')
        objetos  = self.json_data_seed['modelos']["java"]
        for obj in objetos:
            print(template.render(objeto=obj))
            self._prepare_daos_implementados(obj)
        
      
    
