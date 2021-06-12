import cv2 
import matplotlib
import numpy as np
import PIL

################
# SETTINGS
path = './car.jpg'
################


if __name__ == '__main__':
    image = PIL.Image.open(path)

    data  = np.asarray(image)
    print(data.shape)

    length = data.shape[0]
    breadth = data.shape[1]

    new_length = 500
    new_breadth  = int(500 * breadth/length)
    image = image.resize((new_breadth , new_length))
    data = np.asarray(image)
    



    style_file = open('style_file.css','w')
    div_file = open('index.html' , "w")
    length = data.shape[0]
    breadth = data.shape[1]
    print(length)
    print(breadth)
    div_file.write("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style_file.css">
            <title>Document</title>
        </head>
        <body>
            <div id = "container">
    """)

    style_file.write("""
    #container{
        display: grid;
        grid-template-columns: repeat(1000 , 1px);
        grid-template-rows: repeat(1000 , 1px);
        /*background-color: rgb(100, 0, 100);*/
    }
    """)
    for i in range(length):
        for j in range(breadth):
            color_value = "rgb("
            color_value += str(data[i,j,0]) + ","
            color_value += str(data[i,j,1]) + ","
            color_value += str(data[i,j,2]) + ")"

            div_id = "div" + str(i) + 'x' + str(j)

            style_file.write("#" + div_id + "{\n")

            style_file.write("  grid-area: {} / {} / {} / {} ;\n".format(str(i+2) , str(j+2) , str(i+3) , str(j+3)))
            style_file.write("  background-color : {};\n".format(color_value))
            style_file.write("}\n")

            div_file.write("<div id = \"{}\" > </div>\n".format(div_id))

    div_file.write("""
            </div>
        </body>
    </html>
    """)
    style_file.close()
    div_file.close()
