
input = 'train.json'

with open(input) as f:
    content = f.read()
    ann = eval(content)

    pic_dict = {}

    for pic in ann['images']:
        id = pic['id'].split('\\')[-1]
        pic_dict[id] = pic

    for label in ann['annotations']:
        id = label['image_id'].split('\\')[-1]
        pic = pic_dict[id]

        width = pic['width']
        height = pic['height']

        if width < 1 or height < 1:
            print(" wrong image %s reso = %d x %d " %(id, width, height))
            continue 

        x1, y1, w1, h1 = label['bbox']

        c = label['category_id'] - 1
        box_cx, box_cy = (x1 + w1 / 2.0) / width, (y1 + h1 / 2.0) / height
        box_w, box_h = w1 * 1.0 / width, h1 * 1.0 / height

        output = '%s.txt' % id
        with open(output, 'a') as fout:
            line = '%s %f %f %f %f\n' % (c, box_cx, box_cy, box_w, box_h)
            fout.write(line)



