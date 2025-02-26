import pandas as pd
import re

def PGLangs(dataFile) :
    Heared_PGLang_Data = dataFile.iloc[:, 3] # Ngôn ngữ lập trình từng được nghe
    Used_PGLang_Data = dataFile.iloc[:, 6] # Ngôn ngữ lập trình từng sử dụng
    
    Heared_PGLang = {}
    Used_PGLang ={}

    for langs in Heared_PGLang_Data :
        
        langs = re.sub(r'\b\w*[^\x00-\x7F]+\w*\b', '', langs)
        langs = re.sub(r"[\?().]", "", langs)
        langs = re.sub(r"\s*\([^)]*\)", "", langs)
        langs = langs.replace("\\", "")
        langs = langs.replace("/", "")
        langs = langs.replace(",", ";")
        cleandLangs = langs.replace(" ", "").lower().split(";")
        
        for lang in cleandLangs :
            if(lang in Heared_PGLang) :
                Heared_PGLang[lang] = Heared_PGLang[lang] + 1
            else : Heared_PGLang[lang] = 1

    for langs in Used_PGLang_Data : 

        langs = re.sub(r'\b\w*[^\x00-\x7F]+\w*\b', '', langs)
        langs = re.sub(r"[\?().]", "", langs)
        langs = re.sub(r"\s*\([^)]*\)", "", langs)
        langs = langs.replace("\\", "")
        langs = langs.replace("/", "")
        langs = langs.replace(",", ";")
        cleandLangs = langs.replace(" ", "").lower().split(";")
        
        for lang in cleandLangs :
            if(lang in Used_PGLang) :
                Used_PGLang[lang] = Used_PGLang[lang] + 1
            else : Used_PGLang[lang] = 1

    # print(Used_PGLang)
    Heared_PGLang = dict(sorted(Heared_PGLang.items(), key=lambda item: item[1], reverse=True))
    Used_PGLang = dict(sorted(Used_PGLang.items(), key=lambda item: item[1], reverse=True))
    return Heared_PGLang, Used_PGLang

def GetCodeLevel(dataFile) :
    CodeLevel_Data = dataFile.iloc[:, 4] # Trình độ code
    CodeLevel = {}
    
    for level in CodeLevel_Data :
        level = re.sub(r"\s*\([^)]*\)", "", level)  

        if(level in CodeLevel) :
            CodeLevel[level] = CodeLevel[level] + 1
        else : CodeLevel[level] = 1
    
    return CodeLevel