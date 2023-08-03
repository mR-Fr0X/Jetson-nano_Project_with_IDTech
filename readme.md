# Face Detector

The reason I choose this topic as my project is that there are 16 emotions in total, usually people want to know what each other is thinking but it's hard to tell from the outside. Face Detector could help to detect what emotions that person has.

![Result Demo](https://i.imgur.com/VTWSe1j.jpg)

this is what the result should look like (pictures can only show the first 2 digits because it's only 48 pix)

## The Algorithm

In order to start the project, I use resnet18 to train the AI with models from image net. I get my picture from https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer and use them to help with the training

If you want to retrain the model, use the link below to the Google Colab Notebook:
https://colab.research.google.com/drive/1FcBezbuU0YxbLPa5C8fPZofc_15YXblK

## Running this project

1. connect Jetson-nano with VScode using SSH
2. download the files on this page
3. pull the files you want to test under /project/data/face/val
4. change the folder to project by using "cd jetson-inference/project/"
5. run the code "python3 script.py data/face/val data/face/result"
6. after the code is finished, open the folder 'result' to check the result

[View a video explanation here](https://youtu.be/-K0zNkuUm_w)
