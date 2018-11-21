import cv2 

class Video():
    def __init__(self):
        self.capture = cv2.VideoCapture('/home/kanokkorn/Videos/sakura-step.mp4')
        # '/home/kanokkorn/Videos/sakura-step.mp4'
        if not self.capture.isOpened():
            raise RuntimeError('Could not start camera')
    
    def cap_frame(self):
        success, self.frame = self.capture.read()
        ret, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()

if __name__ == '__main__':
    vid = Video()