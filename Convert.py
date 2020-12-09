import json
from pathlib import Path
import re
import sys


class Convert:
    def __init__(self, image_path, json_path):

        self.image_path = image_path
        self.artist = ""
        self.id_number = ""
        self.title = ""
        self.caption = ""
        self.tags = []
        self.page = -1
        self.date = -1
        self.json_path = json_path

    def get_artist(self, artist_name):
        self.artist = artist_name

    def get_id_number(self, id_number):
        self.id_number = id_number

    def get_title(self, title_string):
        if title_string == None:
            pass
        else:
            self.title = title_string

    def get_caption(self, caption_string):
        if caption_string == None:
            pass
        else:
            self.caption = caption_string

    def get_tags(self, tags_list):
        self.tags = tags_list

    def get_page(self):
        #  In order to get the same page number to the nijie one,
        #  we add 1 here.
        path = self.image_path
        file_name = path.name
        if "ugoira" in file_name:
            pass
        else:
            self.page = int(re.search(r"(?<=_p)\d*(?= -)", file_name).group(0)) + 1

    def get_date(self, raw_date_string):

        match = re.search(r"(?<=\d\d\/\d\d\/)\d\d", raw_date_string)
        if match:
            raw_date_year = int(
                re.search(r"(?<=\d\d\/\d\d\/)\d\d", raw_date_string).group(0)
            )
            #  year is stored as 2 digit so we assume if digit is bigger than 90,the picture is in the twentieth century
            #  else it is in the twenty first centry.
            #  this section must be fixed in 2090.
            #  EDIT:2020/11/03 Never mind. They changed date string format yyyy-mm-dd.

            #  remained this if-else section for dealing with old format json.
            if raw_date_year >= 90:
                raw_date_year += 1900
            else:
                raw_date_year += 2000

            raw_date_month = int(
                re.search(r"\d\d(?=\/\d\d\/\d\d)", raw_date_string).group(0)
            )
            raw_date_day = int(
                re.search(r"(?<=\d\d\/)\d\d(?=\/\d\d)", raw_date_string).group(0)
            )

        else:
            raw_date_year = int(
                re.search(r"^\d\d\d\d(?=-\d\d-\d\d)", raw_date_string).group(0)
            )
            raw_date_month = int(
                re.search(r"(?<=^\d\d\d\d-)\d\d(?=-\d\d)", raw_date_string).group(0)
            )
            raw_date_day = int(
                re.search(r"(?<=^\d\d\d\d-\d\d\-)\d\d", raw_date_string).group(0)
            )

        self.date = (
            raw_date_year * (10 ** 4) + raw_date_month * (10 ** 2) + raw_date_day
        )

    def check_escape_letter(self, string):

        escape_letters = {"(", ")", r"\\", "*"}

        for escape_letter in escape_letters:
            if escape_letter in string:
                return True

        return False

    def get_json_path(self):
        """
            returns a json path which has an imformation about the picture.
            return path as Path object
        """

        return self.json_path

    def read_json(self):
        """
            read picture's information from text files
             @param path as path object
        """
        self.json = self.get_json_path()
        informations = self.json.read_text()
        json_informations = json.loads(informations)
        self.get_artist(json_informations["Artist Name"])
        self.get_id_number(json_informations["Image ID"])
        self.get_title(json_informations["Title"])
        self.get_caption(json_informations["Caption"])
        self.get_tags(json_informations["Tags"])
        self.get_page()
        self.get_date(json_informations["Date"])

    def write_txt(self):

        informations = (
            "creator:"
            + str(self.artist)
            + "\n"
            + "id_number:"
            + str(self.id_number)
            + "\n"
            + "title:"
            + str(self.title)
            + "\n"
            + "page:"
            + str(self.page)
            + "\n"
            + "date:"
            + str(self.date)
        )

        for tag in self.tags:
            informations = informations + "\n"
            informations = informations + tag

        picture_path = self.image_path
        picture_mime = picture_path.suffix
        text_path = picture_path.with_suffix(picture_mime + ".txt")

        text_path.write_text(informations)
