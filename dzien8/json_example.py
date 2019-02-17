import json

ds_napis = '{"1":"a"}'

#deserialized
ds_napis = json.loads(ds_napis)
ds_napis["3"] = "f"
ds_napis = json.dumps(ds_napis)
print(ds_napis)

with open("plik.json", "w") as fp:
    json.dump(ds_napis, fp)

with open("plik.json", "r") as fp:
    ob = json.load(fp)
    print(ob)
