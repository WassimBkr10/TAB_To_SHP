import shutil
import sys
import os
sys.path.append(r'C:\Program Files\FME')
sys.path.append(r'C:\Program Files\FME\plugins')
sys.path.append(r'C:\Program Files\FME\python')
sys.path.append(r'C:\Program Files\FME\python\python37')
sys.path.append(r'C:\Program Files\FME\fmeobjects\python37')
try:
    import fmeobjects
except ImportError:
    print("Cannot import")

# initiate FMEWorkspaceRunner Class
PARA = r'C:\WBK\TAB_To_Shp\tab'
runner = fmeobjects.FMEWorkspaceRunner()

# Full path to Workspace, example comes from the FME 2014 Training Full Dataset
workspace = (r'C:\WBK\TAB_To_Shp\scripts\mapinfo2shapefile.fmw')
# Set workspace parameters by creating a dictionary of name value pairs
parameters = {}
parameters['PARAMETER'] = (PARA)

# Use Try so we can get FME Exception
try:
    # Run Workspace with parameters set in above directory
    runner.runWithParameters(workspace, parameters)
    # or use promptRun to prompt for published parameters
    # runner.promptRun(workspace)
except fmeobjects.FMEException as ex:
    # Print out FME Exception if workspace failed
    print(ex.message)
else:
    # Tell user the workspace ran
    print('The Workspace %s ran successfully'.format(workspace))
# get rid of FMEWorkspace runner so we don't leave an FME process running
runner = None


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    # print(allFiles)
    return allFiles

Files = getListOfFiles(PARA)

for file in Files:
    list= ['_point.','_line.','_polygon.','_text.','_geom.']
    for type in list:
        if file.find(type) != -1:
            a= file.replace(type,".")
            try :
               os.rename(file, a)   
            except:
              os.remove(a)
              os.rename(file,a)

