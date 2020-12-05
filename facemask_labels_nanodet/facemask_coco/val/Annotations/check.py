import json 

f = open("val.json", "r")

ret = f.read()

ann = eval(ret)

to_del=[]


for pic in ann['images']:
    if pic['width'] == 0 or pic['height'] == 0:
        to_del.append(pic['id'])
        continue

    if '\\' in pic['file_name']:
        pic['file_name'] = pic['file_name'].split('\\')[-1]


    if '\\' in pic['id']:
        pic['id'] = pic['id'].split('\\')[-1]

new_images=[]
new_annos=[]

for pic in ann['images']:
    if pic['id'] in to_del:
        continue 
    new_images.append(pic)

for pic in ann['annotations']:
    if pic['image_id'] in to_del:
        continue 
    new_annos.append(pic)

ann['images'] = new_images 
ann['annotations'] = new_annos 

for p in ann['annotations']:
    if '\\' in pic['image_id']:
        p['image_id'] = p['image_id'].split('\\')[-1]


s1 = json.dumps(ann)

f = open("val1.json", "w")
f.write(s1)

f.close()


