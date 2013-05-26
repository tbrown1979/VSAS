from vsasGUI.VSASmainScreen import *
from Motion.MotionDetector import *

# def resource_path(relative):
#     return os.path.join(
#         os.environ.get(
#             "_MEIPASS2",
#             os.path.abspath(".")
#         ),
#         relative
#     )

def main():
    motion = MotionDetector()
    motionThread = threading.Thread(None, motion)
    motionThread.daemon = True #daemon threads are background task threads
    motionThread.start()

    vsas = Application(motion, root)
    vsasThread = threading.Thread(None, vsas)
    vsasThread.start()
    
main()
