#encoding=utf-8
#coding=utf-8
import os
import sys
import shutil
import json
import codecs

#源目录地址
SOURCE_FOLDER = "../resources";
TARGET_FOLDER = "../../../web/resource/assets/itempic";
JSON_FILE_NAME = "resource_itempic.json"
JSON_FILE_PATH = "../../../web/resource"
RESOURCE_URL_PREFIX = "assets/itempic/"

def getFiles(dir):
    return os.listdir(dir)

def createJosnConfig(sourceDir):
    resources = []
    for f in getFiles(sourceDir):
        url = "%s%s" % (RESOURCE_URL_PREFIX, f)
        name = "_".join(f.split("."))
        resources.append({
            "url" : url,
            "type" : "image",
            "name" : name
        })
    data = {
        "groups":[],
        "resources":resources
    }   
    out_file = codecs.open(JSON_FILE_NAME, "w", "utf-8")
    json.dump(data, out_file, ensure_ascii=False, indent=2)
    out_file.close()
    filename = os.path.basename(JSON_FILE_NAME)
    shutil.copyfile(JSON_FILE_NAME, os.path.join(JSON_FILE_PATH,filename))
    

#拷贝资源目录文件
def copyFiles(sourceDir, targetDir):
    isExists=os.path.exists(targetDir)
    if not isExists:
        os.makedirs(targetDir)
    for f in getFiles(sourceDir):
        sourceFile = os.path.join(sourceDir, f)
        targetFile = os.path.join(targetDir, f) 
        shutil.copyfile(sourceFile, targetFile)

def getAbspath(path):
    return os.path.abspath(os.path.join(sys.argv[0], path));

def cleanDir(path):
    isExists=os.path.exists(path)
    if isExists:
        shutil.rmtree(path)

if __name__ == "__main__":
    SOURCE_FOLDER = getAbspath(SOURCE_FOLDER)
    TARGET_FOLDER = getAbspath(TARGET_FOLDER)
    JSON_FILE_PATH = getAbspath(JSON_FILE_PATH)

    
    #清理目标目录文件
    print u"1、清理目标目录文件"
    cleanDir(TARGET_FOLDER)
    #拷贝资源文件
    print u"3、拷贝资源文件"
    copyFiles(SOURCE_FOLDER,TARGET_FOLDER)
    #生成json文件
    print u"3、生成配置文件"
    createJosnConfig(SOURCE_FOLDER)
    print u"脚本执行成功"

    