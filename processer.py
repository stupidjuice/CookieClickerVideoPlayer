from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
import os
import math

GOLDENCOOKIE_COL = (0, 0, 0, 255) #black
CLOSENESS_TO_BLACK = 4
RESIZE_X = 28
RESIZE_Y = 21

app = Flask(__name__)
CORS(app)

@app.route("/RenderVideo")
def RenderVideo():
    frames = []

    #for i in range(100):
    for i in range(len(os.listdir('frames/'))):
        currentFrame = []
        zerosToAdd = len(os.listdir('frames/')[0]) - 4 - len(str(i + 1))
        print(i+1)

        img = Image.open("frames/" + '0' * zerosToAdd + str(i + 1) + ".png")
        resized_img = img.resize((RESIZE_X, RESIZE_Y))

        pix_array = resized_img.load()
        for y in range(RESIZE_Y):
            for x in range(RESIZE_X):
                color_r = pix_array[x, y][0]
                if color_r - GOLDENCOOKIE_COL[0] < CLOSENESS_TO_BLACK and color_r + GOLDENCOOKIE_COL[0] > -CLOSENESS_TO_BLACK:
                    currentFrame.append([x * 50, y * 50])
    
        frames.append(currentFrame)          

    Image.open("frames/" + '0' * zerosToAdd + str(i + 1) + ".png").resize((RESIZE_X, RESIZE_Y)).show()
    
    return jsonify({"numFrames": len(os.listdir('frames/')), "frames": frames, "test": "Test Passed"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)