'''
Выведите 'history' из вложенного словаря: 
sampleDict = { 
    "class": { 
        "student": { 
            "name": "Mike", 
            "marks": { 
                "physics": 70, 
                "history": 80 
            } 
        } 
    } 
} 
'''
sampleDict = { 
    "class": { 
        "student": { 
            "name": "Mike", 
            "marks": { 
                "physics": 70, 
                "history": 80 
            } 
        } 
    } 
} 
histori_value = sampleDict["class"]["student"]["marks"]["history"]
print(histori_value)
