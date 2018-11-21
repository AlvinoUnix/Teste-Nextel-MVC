from model.model_nextel import ModelNextel
from view.view_nextel import ViewNextel


# Arquitetura MVC (Model, View e Controller)
class ControllerNextel:
    def nextel(self, input_json_file_path, output_results_file_path):

        model_nextel = ModelNextel()

        view_nextel = ViewNextel()

        json_dictionary = model_nextel.json_reader(input_json_file_path)

        results_dictionary = view_nextel.google_search(json_dictionary)

        model_nextel.json_write(results_dictionary, output_results_file_path)
