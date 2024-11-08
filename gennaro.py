import json
from jinja2 import FileSystemLoader

from generate_code.gen_controller import GenController;
from generate_code.gen_form_html  import GenFormHtml;    
from generate_code.gen_dao        import GenDao;

def gen_all():
    with open('modelo.json', mode='r', buffering=1024, encoding="UTF-8" ) as jr:
        data_seed = jr.read()
        return  json.loads(data_seed)



if __name__ == '__main__':
    json_data_seed = gen_all()
    #gen_form = GenFormHtml(json_data_seed)
    #gen_form.prepare_form()
    #gen_form.prepare_requestDto()
    
    #gen_controller = GenController(json_data_seed)
    #gen_controller.prepare_controller()
    
    gen_dao  = GenDao(json_data_seed)
    gen_dao.prepare_daos() 
            
    
