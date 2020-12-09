import configparser
import os
from pathlib import Path

from FileAggregator import FileAggregator
from Convert import Convert


config = configparser.ConfigParser()
    
config.read('config.ini')
base_path = Path(config['DEFAULT']['FolderPath'])
convert_record = config['DEFAULT']['ConvertRecord']

print("now traversing directories...")
file_list = FileAggregator(base_path)
file_list.load_files()
file_list.is_there_files(base_path)


print("now loading pairs of image and json...")
file_list.filter_out_converted()
pairs_of_image_and_json = file_list.pairs_image_and_json()


print("now writing tags to accompanied text files...")


for pair_of_image_and_json in pairs_of_image_and_json:

    image_path = pair_of_image_and_json[0]
    json_path = pair_of_image_and_json[1]

    #  if file-size is 0.This script stops siliently and files remained not converted.So raise Error and attention.
    if os.path.getsize(image_path) == 0 or os.path.getsize(json_path) == 0:
        print('this file-size is 0.aborting...')
        exit()
    convert = Convert(image_path, json_path)
    print("{0},{1}".format("now converting ", json_path))
    convert.read_json()
    convert.write_txt()

if record_converted:
    file_list.write_converted()
