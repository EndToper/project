# Инверсия картинки => кодирование информации в набор разноцветных пикселей => добавление время создания картинки(ключ) на картинку
# C:\prog\ans.jpg
# 16 бит - 1 символ, 4 пиксиля - 16 бит/1 символ
# шифровка в 4 каналах(RGBA), без учета символов с 254 и 255 в трех каналах(при расшифровки пропускать белые пиксили)


from PIL import Image
import numpy as np
import config
import math

def image_resize(path):
    try:
        with Image.open(path) as img:
            img.load()
        width1, height1 = img.size
        if (width1 > 225):
            img = img.resize((225,height1))
        width, height = img.size
        if (height > 225):
            img = img.resize((width,225))
            width, height = img.size
        if (width1>width or height1 > height):
            new_path = path[0:len(path)-4] + '2' + '.png'
            img.save(new_path, quality=100)
            return new_path
        else:
            return path
    except Exception as e:
        print(e)


def image_resize_big(path):
    try:
        print(path)
        with Image.open(path) as img:
            img.load()
        width1, height1 = img.size
        if (width1 > 500):
            img = img.resize((500,height1))
        width, height = img.size
        if (height > 500):
            img = img.resize((width,500))
            width, height = img.size
        if (width1>width or height1 > height):
            new_path = path[0:len(path)-4] + '2' + '.png'
            img.save(new_path, quality=100)
            return new_path
        else:
            return path
    except Exception as e:
        print(e, 'ошибка 1')




def decrypt(path_of_orig,path):
    try:
        with Image.open(path_of_orig) as img:
            img.load()

        img_array = np.array(img)
        strok, width, pic = np.shape(img_array)
        img_array = np.reshape(img_array, (strok * width, pic))

        with Image.open(path) as img2:
            img2.load()

        img2_array = np.array(img2)
        strok, width, pic = np.shape(img2_array)
        img2_array = np.reshape(img2_array, (strok * width, pic))
        text = ''
        img_len = math.floor(len(img_array) / 4) * 4
        for i in range(0, img_len, 4):
            key = ''
            for p in range(4):
                for k in range(3):
                    key += str(img2_array[i+p][k] - img_array[i+p][k])

            if key != '0'*12:
                if config.dearr[key] != '■':
                    text += str(config.dearr[key])
                if config.dearr[key] == '■':
                    break

        return text
    except Exception as e:
        print(e)


def encrypt(path, string, valid_value, number):
    try:
        with Image.open(path) as img:
            img.load()

        img_array = np.array(img)
        strok, width, pic = np.shape(img_array)
        img_array = np.reshape(img_array, (strok * width, pic))
        str_list = list(string)
        char_num = 0
        img_len = math.floor(len(img_array) / 4) * 4
        for i in range(0, img_len, 4):
            j = int(i / 4)
            if char_num >= len(str_list):
                break

            if valid_value[j]:
                for k in range(3):
                    img_array[i][k] += np.array(config.arr[str_list[char_num]][k]).astype(img_array.dtype)
                    img_array[i + 1][k] += np.array(config.arr[str_list[char_num]][3+k]).astype(img_array.dtype)
                    img_array[i + 2][k] += np.array(config.arr[str_list[char_num]][6+k]).astype(img_array.dtype)
                    img_array[i + 3][k] += np.array(config.arr[str_list[char_num]][9+k]).astype(img_array.dtype)
                char_num += 1

        img_array = np.reshape(img_array, (strok, width, pic))
        img = Image.fromarray(img_array)
        img.save(f'enctryption{number}.png', quality=100)
    except Exception as e:
        print(e)


def make_usable_pixels_array(path):
    try:
        arr = []
        c = 0
        with Image.open(path) as img:
            img.load()

        img_array = np.array(img)
        strok, width, pic = np.shape(img_array)
        print(np.shape(img_array))
        img_array = np.reshape(img_array, (strok * width, pic))
        img_len = math.floor(len(img_array)/4)*4
        for i in range(0, img_len, 4):
            if int(img_array[i][0]) != 255 and int(img_array[i + 1][0]) != 255 and int(img_array[i + 2][0]) != 255 and int(
                    img_array[i + 3][0]) != 255 and int(img_array[i][1]) != 255 and int(img_array[i + 1][1]) != 255 and int(
                img_array[i + 2][1]) != 255 and int(
                img_array[i + 3][1]) != 255 and int(img_array[i][2]) != 255 and int(img_array[i + 1][2]) != 255 and int(
                img_array[i + 2][2]) != 255 and int(
                img_array[i + 3][2]) != 255:
                arr.append(True)
                c+=1
            else:
                arr.append(False)

        return arr, c
    except Exception as e:
        print(e)

#path = r'C:\prog\ans.jpg'
#strr = ' test 5647 fhtgh 5767 семь на восемь тридцать восемь'
#strr += '■'
#val_val, cor_val = make_usable_pixels_array(path)
#print(cor_val)
#img2 = encrypt(path, strr, val_val)
#img2_array = np.array(img2)
#img2.show()
#img2.save(r'C:\prog\ans2.png', quality=100)

#path2 = r'C:\prog\ans2.png'
#t = decrypt(path,path2)
#print(t)