from PIL import Image
import os
import glob 

# source file: 'images\file_with_images'
# output file: 'images\file_with_images_modified'

BASEWIDTH = 800   #  width you wish

def get_files() :
    return glob.glob('images/*/*') # получение массива путей изображений


def create_new_directory(path):
    dir_path = os.path.dirname(os.path.realpath(path)) # получаем старую директорию
    mod_dir = dir_path + '_modified'                   # формируем новую директорию

    if not os.path.isdir(mod_dir):
        os.mkdir(mod_dir)
    return mod_dir

    

def modify_img(path, mod_dir):
    with Image.open(path) as img:
        if img.size[0] > BASEWIDTH:
            img = cut_image(img)
            compress_save(mod_dir, path, img)
        else: 
            filename = path.split('\\')[-1]
            compress_save(mod_dir, path, img)   



def cut_image(image):
    wpersent = (BASEWIDTH/float(image.size[0])) 
    hsize = int(float(image.size[1]) * float(wpersent)) # обрезка с сохранением пропорций
    return image.resize((BASEWIDTH, hsize), Image.Resampling.LANCZOS)



def compress_save(mod_dir, path, img):
    if img.mode != 'RGB':
        img.convert('RGB')
    filename = path.split('\\')[-1]       # достаем имя изображения
    filename = filename.split('.')[0]     # отсекаем расширение изображения

    mod_path = mod_dir + '\\' + filename + '.jpeg'           
    img.save(mod_path, 'JPEG', optimize = True, qality = 80) 

    


def main() :
    paths = get_files()
    mod_dir = create_new_directory(paths[0])  # создаем директорию из пути первого изображения
    for path in paths:
        modify_img(path, mod_dir)

        

if __name__ == '__main__' :
    main()