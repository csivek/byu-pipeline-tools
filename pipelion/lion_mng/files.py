import os
import json
import subprocess



def get_script_path(script_name):
	return os.path.dirname(os.path.realpath(__file__)) + "/sh/" + script_name + ".sh"

def create_directory(path):
    subprocess.check_call([get_script_path("create_directory"), path])

def delete_directory(path):
	subprocess.check_call([get_script_path("delete_directory"), path])

def write_file(directory, name, obj):
    output = open(directory + name, 'w+')
    json.dump(obj, output, indent=3)
    output.close()
