import os
import shutil
import pathlib

main_path = pathlib.Path().resolve()
dir_path = '/plantclef_data'
train_dir = f"{main_path}{dir_path}/train"
test_dir = f"{main_path}{dir_path}/test"

train_class = os.listdir(train_dir)

for clas in train_class :
  if not os.path.exists(f"{test_dir}/{clas}") :
    os.remove(f"{train_dir}/{clas}")

