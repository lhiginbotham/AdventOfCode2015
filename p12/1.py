import json

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

accounting_doc = json.loads(inp[0])

def collect_ints(json_doc):
    if type(json_doc) == int:
        return [ json_doc ]
    elif type(json_doc) == list:
        nums = []
        for obj in json_doc:
            nums += collect_ints(obj)
        return nums
    elif type(json_doc) == dict:
        nums = []
        for obj in json_doc.values():
            nums += collect_ints(obj)
        return nums
    else:
        return []

ints = collect_ints(accounting_doc)
print(sum(ints))
