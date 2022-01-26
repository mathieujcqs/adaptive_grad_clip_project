import os
import re
import cv2
import pathlib
import xml.etree.ElementTree as ET 

dirs = ['/test_1'] # '/train_1', '/train_2', 
main_path = pathlib.Path().resolve()
save_path =['/test'] # '/train',
test_xml_dir = '/GroundTruth'

def get_xml_content(xml_file_path):
  tree = ET.parse(xml_file_path) 
  return tree.find('ClassId').text

def check_if_dir_exists(dir_path):
   if not os.path.isdir(dir_path): 
     os.mkdir(dir_path)
     
for dir in dirs: 
  dir_path = f"{main_path}/{dir}"
  # if dir == dirs[2]:
  xml_dir_path = f"{main_path}{test_xml_dir}"
  # else : 
  #   xml_dir_path = dir_path
    
  jpg_file_list = [ f for f in os.listdir(dir_path) if f.endswith(".jpg") ]
  xml_file_list = [ f for f in os.listdir(xml_dir_path) if f.endswith(".xml") ]
    
  #sorting the files to have the .xml counterparts of.jpg
  jpg_file_list.sort(key=lambda f: int(re.sub('\D', '', f)))
  xml_file_list.sort(key=lambda f: int(re.sub('\D', '', f)))
  
  i=0
  for i in range(len(jpg_file_list)):
    image_file = jpg_file_list[i]
    xml_file = xml_file_list[i]
    print(xml_file)
    species = get_xml_content(f"{xml_dir_path}/{xml_file}")
    img = cv2.imread(f"{dir_path}/{image_file}")

    #downsizing img to our net input_shape
    res = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
    
    #saving image to its new folder
    # if dir == dirs[0] or dir == dirs[1]:
    #   species_path = f"{main_path}{save_path[0]}/{species}"
    #   check_if_dir_exists(species_path)
    #   cv2.imwrite(f"{species_path}/{image_file}",res)
    # else :
    species_path = f"{main_path}{save_path[0]}/{species}"
    check_if_dir_exists(species_path)
    cv2.imwrite(f"{species_path}/{image_file}",res)
    i+=1
