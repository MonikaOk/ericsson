import Read
import Write

if __name__ == '__main__':
    file_input_name = "input.txt"
    file_output_name = "output.txt"
    objects = Read.read_file(file_input_name)
    Write.generate_output(file_output_name, objects)
