from tkinter import Tk
from owlready2 import *
from os.path import abspath, dirname, join
#from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os


def findInstanceWithLabel(classRef, label):
    for inst in classRef.instances():                                           # ищу в классе classRef экземпляр с label равным label
        if inst.label and (inst.label[0] == label):                             # если такой экземпляр найден, то возвращаю его
            return inst
    return False

def createInstanceWithLabel(classRef, label):
    inst = classRef()
    inst.label = label
    return inst

def createRepresentedVariableValues(className, labels, representedVariableInstance):
    print(className)
    print(labels)
    print(representedVariableInstance)
    classRef = empirionClasses["RepresentedVariableValue"]
    for label in labels:
        fullLabel=className+";"+label
        print(fullLabel)
        inst = findInstanceWithLabel(classRef, fullLabel)
        print(inst)
        if not inst:
            with namespace:
                inst=createInstanceWithLabel(classRef, fullLabel)
                print(inst)
                representedVariableInstance.hasValueDomain.append(inst)
    return True

def typeA(items):
    # имя класса переменной
    className = items[1]
    # делим описание представлений на пары "представление - 'идеальное' значение"
    pairs = items[2].split(";")
    # получаем строку из отсортированных пар, чтобы потом подставлять ее в label экземпляров className+"Representation"
    pairs.sort()
    representationLabel = ";".join(pairs)
    # создаем списки представлений и 'идеальных' значений, а также словарь вида "представление: 'идеальное' значение"
    representationLabels = []
    representedVariableLabels = []
    dictLabels = {}
    for pair in pairs:
        pairList = pair.split("-")
        representationLabels.append(pairList[0])
        representedVariableLabels.append(pairList[1])
        dictLabels[pairList[0]]=pairList[1]
    # сортируем список 'идеальных' значений
    representedVariableLabels.sort()
    # формируем название существующего экземпляра подкласса RepresentedVariable, а затем получаем сам экземпляр по его имени
    reprVarInstanceName = (className+"RepresentedVariable1").lower()
    reprVarInstance = empirion[reprVarInstanceName]
    # создаем все недостающие экземпляры класса RepresentedVariableLabels и связываем их с reprVarInstance
    createRepresentedVariableValues(className, representedVariableLabels, reprVarInstance)
    #empirion[reprVarInstanceName].label = ";".join(representedVariableLabels)  - не работает, так как не в нашей онтологии
    # получаем подкласс variable по его имени
    variableClass = empirionClasses[className]
    # получаем подкласс representation по его имени
    represenationClass = empirionClasses[className+"Representation"]                

    with namespace:
        # в namespace создаю экземпляр variable с именем по умолчанию и label, в котором указываю имя столбца
        variableInstance = createInstanceWithLabel(variableClass, items[0])
        # создаю отношение variable между datafileN и variableN
        dataFile.variable.append(variableInstance)                                  
        # ищу в подклассе representation экземпляр с label равным representationLabel
        representationInstance = findInstanceWithLabel(represenationClass, representationLabel)
        # если такой экземпляр найден, то создаю отношение representation между variableN и этим экземпляром
        if representationInstance:                                                         
            variableInstance.representation.append(representationInstance)
        # если такого экземпляра еще нет, то:
        else:                                                                       
            representationInstance = createInstanceWithLabel(represenationClass, representationLabel)
            variableInstance.representation.append(representationInstance)
            representationInstance.basedOn.append(reprVarInstance)
            for item in representationLabels:
                inst = findInstanceWithLabel(empirionClasses["RepresentationValue"],className+";"+item)
                if inst and (inst.represents.label[0]==className+";"+dictLabels[item]):
                    representationInstance.hasValueDomain.append(inst)
                else:
                    inst = createInstanceWithLabel(empirionClasses["RepresentationValue"], className+";"+item)
                    representationInstance.hasValueDomain.append(inst)
                    instSameAs = findInstanceWithLabel(empirionClasses["RepresentedVariableValue"],className+";"+dictLabels[item])
                    inst.represents = instSameAs
    return True

def typeB(items):
    className = items[1]
    valueDomain = items[2]
    print("typeB: "+className)
    variableClass = empirionClasses[className]                                      # получаю подкласс variable по его имени
    represenationClass = empirionClasses[className+"Representation"]                # получаю подкласс representation по его имени
    reprVarInstanceName = (className+"RepresentedVariable1").lower()                # формирую название экземпляра подкласса RepresentedVariable
    with namespace:
        variableInstance = createInstanceWithLabel(variableClass, items[0])
        dataFile.variable.append(variableInstance)                                  # создаю отношение variable между datafileN и variableN
        representationInstance = findInstanceWithLabel(represenationClass, valueDomain)                   # ищу в подклассе representation экземпляр с label равным valueDomain
        if representationInstance:                                                         # если такой экземпляр найден, то:
            variableInstance.representation.append(representationInstance)                            # создаю отношение representation между variableN и этим экземпляром
        else:                                                                       # если такого экземпляра еще нет, то:
            representationInstance = createInstanceWithLabel(represenationClass, valueDomain)
            variableInstance.representation.append(representationInstance)          # создаю отношение representation между variableN и representationN
            representationInstance.basedOn.append(empirion[reprVarInstanceName])    # создаю отношение basedOn между representationN и _representedvariable1
            instUnit = findInstanceWithLabel(empirionClasses["MeasurementUnit"],valueDomain)
            if not instUnit:                                                         # если такой экземпляр найден, то:
                instUnit = createInstanceWithLabel(empirionClasses["MeasurementUnit"], valueDomain)
            representationInstance.hasMeasurementValue.append(instUnit) 
    return True

def typeC(items):
    className = items[1]
    variableClass = empirionClasses[className]                                      # получаю подкласс variable по его имени
    represenationClass = empirionClasses[className+"Representation"]                # получаю подкласс representation по его имени
    reprVarInstanceName = (className+"RepresentedVariable1").lower()                # формирую название экземпляра подкласса RepresentedVariable
    with namespace:
        variableInstance = createInstanceWithLabel(variableClass, items[0])
        dataFile.variable.append(variableInstance)                                  # создаю отношение variable между datafileN и variableN
        representationInstance = createInstanceWithLabel(represenationClass, className)
        variableInstance.representation.append(representationInstance)              # создаю отношение representation между variableN и representationN
        representationInstance.basedOn.append(empirion[reprVarInstanceName])        # создаю отношение basedOn между representationN и _representedvariable1
    return True

root = Tk()
root.withdraw()


#filename = filedialog.askopenfilename()
#print(filename)
#onto_path.append(dirname(filename))
#print(dirname(filename))
#filename="ontomorf.owl"
#onto = get_ontology(filename).load()

onto_path.append(r"C:\Users\Alena\Desktop\empirion2_exp")                     # указываю путь к локальной папке, в которой хранится онтология
onto = get_ontology("empirion_pop.owl").load()               # загружаю локальную онтологию (иначе ее не сохранить)
namespace = onto                                            # задаю namespace, который буду использовать для создания экземпляров и отношений
empirion = onto.imported_ontologies[0]                      # получаю онтологию empirion
empirionClasses = dict()
for entity in list(empirion.classes()):                     # строю словарь классов онтологии emprion, чтобы к ним было удобно обращаться по имени
    empirionClasses[entity.name]=entity

empirion2 = empirion.imported_ontologies[0]  
for entity in list(empirion2.classes()):                     # строю словарь классов онтологии emprion, чтобы к ним было удобно обращаться по имени
    empirionClasses[entity.name]=entity
print (empirionClasses)
work_directory = askdirectory()                             # спрашиваю у пользователя, в какой папке лежат файлы с описанием
os.chdir(work_directory)                                    # делаю эту папку текущей

for f_name in os.listdir(work_directory):                   # пробегаю по всем файлам этой папки
    if f_name.endswith('_toonto.txt'):                      # рассматриваю только файлы, имена которых заканчиваются на _toonto.txt
        print(f_name)
        with open(f_name,'r') as file:                      # открываю файл
            #-----------------------------------------------------------------------------------------------------------------------------#
            # Блок1
            #-----------------------------------------------------------------------------------------------------------------------------#
            first = file.readline()                         # читаю первую строку
            dataFileStr = first.split()[1]                  # получаю имя DataFile 
            print(dataFileStr)
            dataFileClass = empirionClasses['DataFile']     # получаю класс DataFile из онтологии empirion
            with namespace:
                dataFile = dataFileClass()                  # в namespace создаю экземпляр класса DataFile с именем по умолчанию 
                dataFile.label = dataFileStr                # добавляю label, в котором указываю имя файла
            print(dataFile)
            #-----------------------------------------------------------------------------------------------------------------------------#
            # Блок2
            #-----------------------------------------------------------------------------------------------------------------------------#            
            second = file.readline()                        # читаю вторую строку
            varDescrStr = second.split()[1]                 # получаю имя VariableDescription 
            print(varDescrStr)
            varDescrClass = empirionClasses['VariableDescriptionFile'] # получаю класс VariableDescriptionFile из онтологии empirion
            print(varDescrClass)
            with namespace:
                varDescr = varDescrClass()                  # в namespace создаю экземпляр класса VariableDescriptionFile с именем по умолчанию 
                varDescr.label = varDescrStr                # добавляю label, в котором указываю имя файла
                dataFile.metadata.append(varDescr)          # создаю отношение metadata между datafileN и variabledescriptionN
            print(varDescr)
            #-----------------------------------------------------------------------------------------------------------------------------#
            # Блок3
            #-----------------------------------------------------------------------------------------------------------------------------#
            line = file.readline()                          # читаю третью строку
            line = file.readline()                          # читаю четвертую строку
            line = file.readline()                          # читаю пятую строку
            while line:                                     # читаю строки в цикле, пока не закончатся
                if not line.startswith("#"):                # фильтрую строки, начинающиеся с решетки, считая их комментариями
                    columns = line.split()                    # разбиваю строку на подстроки по разделителю по умолчанию
                    if (len(columns) == 2):                   # если получилось 2 подстроки, то вызываю функцию typeC
                        typeC(columns)
                    elif (len(columns) == 3):
                        items = columns[2].split(";")
                        if (len(items) == 1):
                            print(columns)
                            typeB(columns)
                        else:
                            typeA(columns)
                    else:
                        print("Ошибка в файле _toonto")
                line = file.readline()
onto.save()
