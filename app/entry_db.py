# reads db.json and builds gallery entry objects
# each entry has a render html method which creates its html page.
# the Db class holds all entries and can render the index page.
# each entry is stored on disk as a json object.
# would it be better to store the db in the file system with each folder containing the image and txt file? maybe.
# actually yeah having each entry in its own folder with a json file and image file is probably better it makes it easier to modify, 
# only problem is it makes data and potentially large images intertwinned
# i could make a hybrid approach where there are single json files for each entry but the images are stored in a single folder
# which could be excluded from git. 
# however this makes it read disk more. and or access more disk at startup. 
# massive jsons are harder to edit manually though, i could make a helper script to add entries.
# so manually, fs based is better, efficiently and programmatically, single json is better.
# ill probably use single json for now and see how it goes.
# in which case ill make the helper script, itll import this module and use it to add and load entries.
# would i make it interactive or just take command line args? idk id probably prefer interactive since its a lot of data.

# should the images be flat or in subfolders? for organization subfolder would be better but it makes it harder to see at an overview.
# forgot that im also gonna have element collection photos, where the camera data doesnt really matter.
# so maybe ill have either, an enum object for astro/element specific data as the html pages will be rendered differently anyways.
# 
# oh i could just read from the exif data of the image to fill in the camera data, that would be way easier.
# however idk if it knows the lens used, and i want to be able to specify the lens.
# so entry might be more of an exif reader and then it presents you with the data it found then you can change it
# or add to it for missing fields. + add title and description.
# so first, input a file path, it then copies the file to the images folder, reads exif data,
# presents you with the data. then lets you write description and title.
# then it saves the entry to the json db.
# image file could be cmd arg. each pos-arg could be an image and it just queues them up.
# could be tui or just interactive cli, or tkinter gui. since its just for me ill probably just do cli.
# if i make the images organized in subfolders, then well..... oh i know ! category field!! 
# the program will copy into static/images/<category>
# i probably want to include full res images as well, so maybe static/images/full and static/images/thumbs
# and it will make the thumbs automatically.

# so you run the script with element or astro as argv[1] then a list of image paths, it reads the exif data, compresses, asks for category, title, description.
# stores full res in static/images/full/<category>/ and thumb in static/images/<elements|astro>thumbs/<category>/

from dataclasses import dataclass
import json
# class 
@dataclass
class GalleryEntry:
    
    title:str
    description:str
    image_thumb:str    
    image_full:str
    
def int_input(prompt:str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

class Db:
    def __init__(self, json_file:str) -> None:
        self.json_file = json_file
