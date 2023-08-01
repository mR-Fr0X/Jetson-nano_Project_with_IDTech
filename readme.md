# Face Detector

Face Detector is used to detect what emotion the person have

![Collage Maker-31-Jul-2023-04-54-PM-43997](https://github.com/mR-Fr0X/Jetson-nano_Project_with_IDTech/assets/140645291/9ef2fc4f-95e8-46b2-b360-d8616d2b09bf)

this is what the result should look like (3 of them are all from happy but because the picture is only 48 pix)

## The Algorithm

In order to start the project, I use resnet18 to train the AI with models from image net. I get my picture from https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer and use them to help with the training

## Running this project

1. connect Jetson-nano with VScode using SSH
2. download the files on this page
3. pull the files you want to test under /project/data/face/val
4. change the folder to project by using "cd jetson-inference/project/"
5. run the code "python3 script.py data/face/val data/face/result"
6. after the code is finished, open the folder 'result' to check the result

[View a video explanation here](video link)
