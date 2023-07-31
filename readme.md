# Face Detector

Face Detector is use when people are unable to know what solution they are in > 

![https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.research-live.com%2Fimg%2Femotions_crop.jpg&tbnid=u-bD9o_XVDii_M&vet=12ahUKEwjxvKfQtbmAAxV-hu4BHTVgAAkQMygBegUIARDdAQ..i&imgrefurl=https%3A%2F%2Fwww.research-live.com%2Farticle%2Fopinion%2Fface-up-to-it-emotion-detection-transforms-market-research-%2Fid%2F5006942&docid=fbSMkMAt0pTinM&w=592&h=444&q=human%20face%20emotion&ved=2ahUKEwjxvKfQtbmAAxV-hu4BHTVgAAkQMygBegUIARDdAQ](direct image link here)

## The Algorithm

Inorder to start the project, i use resnet18 to train the AI with models from image net. i get my picture from https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer, and use them to help with the trainings

## Running this project

1. connect Jetson-nano with VScode using SSH
2. download the files at this page
3. pull the files u want to test under /project/data/face/val
4. chenge the folder to project by using "cd jetson-inference/project/"
5. run the code "python3 script.py data/face/train/ data/face/result"
6. after the code is finish, open the folder 'result' to check the result

[View a video explanation here](video link)
