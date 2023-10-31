#!/usr/bin/env python3

import os
import requests

feedback_dir =  "D:\\QA\python\\feedback" # varible with path
feedback_list = os.listdir(feedback_dir) # creating list of files with feedbacks
feedback_all = [] # list od all dicteonary deedback

for files in feedback_list : # Create dict w feedback content 
    file_open =  os.path.join(feedback_dir, files)
    with open(file_open, "r") as feedback :
        content_list = [] #read line by line  creating value for dictionary
        for line in feedback:
            content_list.append(line)
        feedback_dict ={"title": content_list[0], "name": content_list[1], "date": content_list[2], "feedback": content_list[3]}
        feedback_all.append(feedback_dict) #add dict to feedback dict list
print (feedback_all)
