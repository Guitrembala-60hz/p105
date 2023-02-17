import os
import cv2
path = "png"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
out = cv2.VideoWriter('project3.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#Para o PÔR DO SOL
#for i in range(0,count-1):

#Para o NASCER DO SOL
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    print(images[i])
    
out.release() # liberando o vídeo gerado
print("Concluído")
