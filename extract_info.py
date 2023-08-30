import easyocr
import os
import cv2
import sys

def extract_all(input_dir, output_dir):
    reader = easyocr.Reader(['en'])
    count = 0
    image_format = [".jpg", ".jpeg", ".bmp", ".png"]
    file_list = os.listdir(input_dir)
    file_list.sort()
    for i in range(0, len(file_list)):
        # print("[{}/{}] ".format(i+1, len(file_list)), end='')
        in_path = os.path.join(input_dir, file_list[i])

        if os.path.isfile(in_path):
            if os.path.splitext(in_path)[1] not in image_format:
                print("{} is not an acceptable image file, please use .jpg/.jpeg/.bmp/.png as input.".format(file_list[i]))
                continue
        else:
            continue

        global name
        name = os.path.splitext(file_list[i])[0]
        out_path = os.path.join(output_dir, name + ".png")
        
        try:
            result = reader.readtext(in_path)
            print(result)
        except:
            continue

        
        


def extract(input_path, output_path):
    reader = easyocr.Reader(['en'])
    image_format = {".jpg", ".jpeg", ".bmp", ".png"}
    if os.path.isfile(input_path):
        if os.path.splitext(input_path)[1] not in image_format:
            print("Parameters Error: invalid input or output.")
            sys.exit()
    else:
        print("Parameters Error: invalid input or output.")
        sys.exit()

    global name
    name = os.path.splitext(os.path.basename(input_path))[0]

    try:
        result = reader.readtext(input_path)
        print(result)
    except:
        pass
    

        
    
    