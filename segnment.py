import os
from PIL import Image

def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <=w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('图片切割')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c*colwidth, r*rowheight, (c+1)*colwidth, (r+1)*rowheight)
                img.crop(box).save(os.path.join(dstpath, '1_' + basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('共生成 %s 张图片' % num)
    else:
        print('error')

def mkdir(path):
    path = path.strip()
    path = path.rstrip('\\')
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+"success")
        return True
    else:
        print(path+'exist')
        return False

folder = r'ebsd/2x'
path = os.listdir(folder)
for each_bmp in path:
    first_name, second_name = os.path.splitext(each_bmp)
    each_bmp = os.path.join(folder, each_bmp)
    src = each_bmp
    print(src)
    mkpath = 'ebsd/2x_segnment'
    mkdir(mkpath)
    if os.path.isfile(src):
        dstpath = mkpath
        if (dstpath == '') or os.path.exists(dstpath):
            row = int(4)
            col = int(4)
            if row > 0 and col > 0:
                splitimage(src, row, col, dstpath)
            else:
                print('no')
        else:
            print('not exist')



