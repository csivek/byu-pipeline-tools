
import json
import subprocess


def load_hierarchies_file():
    return json.load(open("../hierarchy.json"))

def get_root_directory():
    #add a ../ because we're a directory down from hierarchy.json
    return "../" + load_hierarchies_file()['root']

def get_raw_assets():
    return load_hierarchies_file()['children']

def init_all_assets():
    raw_assets = get_raw_assets()

    for asset in raw_assets:
        create_asset(asset)


def create_asset(assetJson):
    root = get_root_directory()
    asset_path = assetJson['location']
    subprocess.check_call(["sh/init_asset.sh", root, assetJson['name'], asset_path])
    body_output = open(root + "/" + asset_path + "/" + "body.json", 'w')
    assetBody = {}
    assetBody['name'] = assetJson['name']
    assetBody['departments'] = []
    assetBody['steps'] = []
    json.dump(assetBody, body_output, indent=4)
    body_output.close()


init_all_assets()
