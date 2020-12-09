from collections import defaultdict
import json
import pathlib 
import re
import sys

class FileAggregator:

    def __init__(self, path):
        '''
            @param path as Path object
        '''
        self._root_path = path
        self._file_paths = []
        self._not_converted_files = set()
        self.id_to_files_dictionary = defaultdict()

    def aggregates_files(self, _root_path):
        '''
            Aggregate picture files and text files from a selected folder recursively
            @param root_path as path object
            @yield Found file path as path object
        '''
        if _root_path.is_dir():
            for path in _root_path.iterdir():
                for item in self.aggregates_files(path):
                    yield item
        else:
            yield _root_path

    def load_files(self):
        self._file_paths = [ path for path in self.aggregates_files(self._root_path) if path.suffix != '.txt' and path.suffix != '.zip']

    def load_file_path_list(self):
        return self._file_paths

    def pack_same_id_paths(self, path):
        path_name = path.name
        id_num = re.match(r'^[0-9]*(?=\_)', path_name)
        try:
            if id_num.group() in self.id_to_files_dictionary.keys():
                self.id_to_files_dictionary[id_num.group()].append(path)
            else:
                self.id_to_files_dictionary[id_num.group()] = [path]
        except:
            pass


    def pairs_image_and_json(self):
        #collect same id image and json files
        for path in self._not_converted_files:
            self.pack_same_id_paths(path)
        pairs_of_image_and_json = []
        #find a json path
        for files_with_same_id in self.id_to_files_dictionary.values():
            for path in files_with_same_id:
                if path.suffix == '.json':
                    json_path = path

        #pair the json path to an image path
        #pair is a tuple and image path comes first and json path comes second
            for path in files_with_same_id:
                if path.suffix != '.json':
                    pairs_of_image_and_json.append((path,json_path))

        return pairs_of_image_and_json

    def load_converted(self):
        with open("converted_list.json") as f:
            converted_files = json.load(f)
        converted_files = list(map(Path, converted_files))
        return converted_files

    def write_converted(self):
        file_path_list = self.load_file_path_list()
        with open("converted_list.json", "w") as f:
            json.dump(file_path_list, f, default=self.posix_path_default,indent=4)

    def filter_out_converted(self):
        '''
            exclude already converted file paths from loaded file list
        '''
        try:
            converted_files = load_converted()
        except:
            converted_files = []
        converted_files_set = set(converted_files)
        files_set = set(self._file_paths)

        self._not_converted_files = files_set - converted_files_set
    
    def is_there_files(self, base_path):
        if self._file_paths == [base_path]:
            print("there's no new files")
            print("exiting...")
            exit()
        else:
            print("there's new files")

