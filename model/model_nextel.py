import json


class ModelNextel:
    def json_reader(self, input_json_directory):
        return json.loads(open(input_json_directory).read())


    def json_write(self, results_dictionary, output_results_file_path):

        with open(output_results_file_path, "w") as write_file:
            json.dump(results_dictionary, write_file, ensure_ascii=False, indent=4)
