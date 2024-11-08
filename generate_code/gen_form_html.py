from jinja2 import Environment, FileSystemLoader

class GenFormHtml(object):

    def __init__(self, data_seed):
        self.data_seed = data_seed
        file_loader = FileSystemLoader('templates')
        self.env = Environment(loader=file_loader)

    def prepare_form(self):
        template = self.env.get_template('form_html.txt')
        data_form = self.data_seed["modelos"]["form_controller"]
        print(template.render(tags=data_form))
    
    def prepare_requestDto(self):
        template = self.env.get_template('fom_request_class.txt')
        data_form = self.data_seed["modelos"]["form_controller"]
        request_backend_class=self.data_seed["modelos"]["form_class"]
        print(template.render(fields=data_form, request_class=request_backend_class))