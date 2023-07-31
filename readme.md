# Face Detector

Face Detector is use when people are unable to know what solution they are in > 

![](direct image link here)

## The Algorithm

Inorder to start the project, I use resnet18 to train the AI with models from image net. I get my picture from https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer, and use them to help with the trainings

## Running this project

1. connect Jetson-nano with VScode using SSH
2. download the files at this page
3. pull the files you want to test under /project/data/face/val
4. chenge the folder to project by using "cd jetson-inference/project/"
5. run the code "python3 script.py data/face/train/ data/face/result"
6. after the code is finish, open the folder 'result' to check the result

[View a video explanation here](video link)
