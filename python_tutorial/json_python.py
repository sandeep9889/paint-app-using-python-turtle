#javascript object notation
# json used to send aur export data from web
import json 
data = '{"varr1":"sandeep", "varr2":"jatin"}'
parsed =json.loads(data)
print(parsed["varr1"])
print(data)
data2 = {
    "chennal_name": "code with harry",
    "cars": ['bmw','audi-a8','ferrari'],
    "fridge":('roti',540),
    "isbad": False
}
jscomb = json.dumps(data2)
print(jscomb)