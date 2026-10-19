import pymupdf, os

doc = pymupdf.open('1151019-115南投國二露營手冊.pdf')
target_pages = [13, 14, 15, 16, 17, 18, 21, 22, 23]

for p_num in target_pages:
    page = doc[p_num - 1]
    img_list = page.get_images()
    print(f'Page {p_num}: {len(img_list)} images')
    for i, img_info in enumerate(img_list):
        xref = img_info[0]
        base_img = doc.extract_image(xref)
        img_bytes = base_img['image']
        img_ext = base_img['ext']
        w = base_img['width']
        h = base_img['height']
        img_filename = f'assets/p{p_num}_img{i+1}.{img_ext}'
        with open(img_filename, 'wb') as f:
            f.write(img_bytes)
        print(f'  Saved {img_filename} ({w}x{h})')
