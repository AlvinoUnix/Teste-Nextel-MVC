from controller.controllernextel import ControllerNextel


#Classe principal do robô
class Run:
    def controller_caller(cls, input_json_file_path, output_results_file_path):
        controller_nextel = ControllerNextel()
        controller_nextel.nextel(input_json_file_path, output_results_file_path)

input_json_file_path = 'input.json'
output_results_file_path = 'output.json'
run = Run()
run.controller_caller(input_json_file_path, output_results_file_path)
