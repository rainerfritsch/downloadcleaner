import os
from pathlib import Path
from configparser import ConfigParser
import argparse


parser = ConfigParser()
parser.read('./config.ini')

# config 
# ändern zu https://www.geeksforgeeks.org/python-os-path-join-method/

baseDirectory = str(Path.home())+os.sep
downloadDirectory = baseDirectory + parser.get("folder", "downloadDirectory")
documentDirectory = downloadDirectory + parser.get("folder", "documentDirectory")
pictureDirectory = downloadDirectory + parser.get("folder", "pictureDirectory")
installationDirectory= downloadDirectory + parser.get("folder", "installationDirectory")
musicDirectory = downloadDirectory + parser.get("folder", "musicDirectory")
videoDirectory = downloadDirectory + parser.get("folder", "videoDirectory")
archiveDirectory = downloadDirectory + parser.get("folder", "archiveDirectory")



argParser = argparse.ArgumentParser()
argParser.add_argument('-l','--location', help='Cleanup Desktop or Downloads')

args = argParser.parse_args()

if args.location is not None:
    location=args.location
    print("Selected location " + location)

# files ending with this ending fall into that category
txtfiles=parser.get("sorting", "txtfiles")
musicfiles=parser.get("sorting", "musicfiles")
installationfiles=parser.get("sorting", "installationfiles")
videofiles=parser.get("sorting", "videofiles")
picturefiles=parser.get("sorting", "picturefiles")
archivefiles=parser.get("sorting", "archivefiles")

# decide if file ends with given fileending
def kindOf(filename, endings):
    isKindOf=0
    aendings=endings.split(",")
    for ending in aendings:
        if filename.endswith(ending):
            isKindOf=isKindOf+1
    #if filename ends with certain filending return true
    return (isKindOf>0)

# create folders if nessesary
def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)

def check():
    assure_path_exists(documentDirectory)
    assure_path_exists(pictureDirectory)
    assure_path_exists(installationDirectory)
    assure_path_exists(musicDirectory)
    assure_path_exists(videoDirectory)
    assure_path_exists(archiveDirectory)

# let´s go
def main():
    check()
    for filename in os.listdir(downloadDirectory):
        if (kindOf(filename,txtfiles)):
            print ("*Textfile found * "+filename)
            os.rename(downloadDirectory+filename,documentDirectory+filename)
        if (kindOf(filename,musicfiles)):
            print ("*Music found * "+filename)
            os.rename(downloadDirectory+filename,musicDirectory+filename)
        if (kindOf(filename,installationfiles)):
            print ("*Installation file found * "+filename)
            os.rename(downloadDirectory+filename,installationDirectory+filename)
        if (kindOf(filename,videofiles)):
            print ("*Video file found * "+filename)
            os.rename(downloadDirectory+filename,videoDirectory+filename)
        if (kindOf(filename,picturefiles)):
            print ("*Picture file found * "+filename)
            os.rename(downloadDirectory+filename,pictureDirectory+filename)
        if (kindOf(filename,archivefiles)):
            print ("*Picture file found * "+filename)
            os.rename(downloadDirectory+filename,archiveDirectory+filename)

if __name__ == "__main__":
  
  main()
