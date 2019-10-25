import os, os.path

import xmltodict as xml

import pandas as pd

def change_dir(dir):
    os.chdir(dir)
    return dir

change_dir(input("enter the directory name: "))

with open('test.xml') as input_xml:

    dictionary = xml.parse(input_xml.read())

df = pd.DataFrame.from_dict(dictionary)

export_csv = df.to_csv('C:/Users/johna/Desktop/Python/XML Files/test.csv')

#Directory: /Users/johna/Desktop/Python/XML Files