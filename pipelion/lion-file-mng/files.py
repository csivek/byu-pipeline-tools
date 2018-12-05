
import json
import subprocess

def open_hierarchies_file():
    return open("../hierarchy.json")

def add_to_hierarches_file(asset):
    hierarches = load_hierarchies_file()
    hierarchies['children'].append(asset)
    output = open_hierarchies_file()
    json.dump(hierarchies, output, indent=4)
    output.close()

def load_hierarchies_file():
    return json.load(open_hierarchies_file())

def get_root_directory():
    #add a ../ because we're a directory down from hierarchy.json
    return "../" + load_hierarchies_file()['root']

def get_raw_assets():
    return load_hierarchies_file()['children']

def init_all_assets():
    raw_assets = get_raw_assets()

    for asset in raw_assets:
        create_asset_directory(asset['location']

def delete_asset(asset_body):
    root = get_root_directory()
    subprocess.check_call(["sh/delete_directory.sh", root, asset_path])

def create_asset_directory(asset_path):
    root = get_root_directory()
    subprocess.check_call(["sh/create_directory.sh", root, asset_path])

#warning: will overwrite whatever is already there
def create_asset(asset_body):
    add_to_hierarches_file(asset_body)
    asset_path = asset_body['path'] #TODO is this the right name for the path?
    create_asset_directory(asset_path)
    body_output = open(root + "/" + asset_path + "/" + "body.json", 'w')
    json.dump(asset_body, body_output, indent=4)
    body_output.close()


asset_body =
