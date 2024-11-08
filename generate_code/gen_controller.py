from jinja2 import Environment, FileSystemLoader

class GenController(object):

    def __init__(self, json_data):
        self.json_data_seed = json_data
        file_loader = FileSystemLoader('templates')
        self.env = Environment(loader=file_loader)
        
   
    def prepare_controller(self):
        template = self.env.get_template('controller.txt')
        full_data  = self.json_data_seed['modelos']
        print(template.render(controller_config=full_data))
      
    
