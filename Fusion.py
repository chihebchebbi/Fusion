import json
import os

banner = """
FUSION: MITRE ATT&CK NAVIGATION LAYER COMBINER
"""
print(banner)
Local_Path = input("[+] Enter the path to the local MITRE ATT&CK Navigation Layer files: ") 
if Local_Path[-1] != "/":
    Local_Path = Local_Path+"/"

Thechniques = []
Nav_Layers  = [pos_raw for pos_raw in os.listdir(Local_Path) if pos_raw.endswith('.json')]
for layer in Nav_Layers:
    try:
        with open(Local_Path+layer,'r',) as l:
            techs = json.load(l)
    except:
        pass
    for i in range(len(techs["techniques"])):
        #print(techs["techniques"][i]["techniqueID"])
        Thechniques.append(techs["techniques"][i]["techniqueID"])
    
Thechniques =  list(dict.fromkeys(Thechniques)) # Remove Duplicates

# Generate MITRE Layer

Layer_Template = {
    "description": "Techniques Covered by Azure Sentinel Rules and Queries",
    "name": "Azure Sentinel Coverage",
    "domain": "mitre-enterprise",
    "version": "4.5",
    "techniques": 
		[{  "techniqueID": technique, "color": "#ff0000"  } for technique in Thechniques] 
    ,
    "gradient": {
        "colors": [
            "#ffffff",
            "#ff0000"
        ],
        "minValue": 0,
        "maxValue": 1
    },
    "legendItems": [
        {
            "label": "Techniques Covered by Azure Sentinel",
            "color": "#ff0000"
        }
    ]
}

json_data = json.dumps(Layer_Template)

Output_File = input("[+] Enter the name of the output file: ")

with open(Output_File+".json", "w") as file:
    json.dump(Layer_Template, file)

print("[+] The MITRE matrix json file "+Output_File+" was created successfully")
