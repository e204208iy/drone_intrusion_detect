from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2

model = YOLO("sawada_130.pt")

cap = cv2.VideoCapture("./videos/4sec.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

region_points = [(750, 560), (1130, 560), (1130, 650), (750, 650)]
region_points_2 = [(680, 490), (1200, 490), (1200, 720), (680, 720)]

# region_points = [(120, 120), (120, 120), (120, 120), (120, 120)]
# region_points_2 = [(120, 120), (120, 120), (120, 120), (120, 120)]
video_writer = cv2.VideoWriter("object_counting_output.mp4",
                       cv2.VideoWriter_fourcc(*'mp4v'),
                       fps,
                       (w, h))

# Init Object Counter
counter = object_counter.ObjectCounter()
counter.set_args(view_img=True,
                 reg_pts=region_points,
                 reg_pts_2=region_points_2,
                 classes_names=model.names,
                 draw_tracks=True)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    #tracks = model.track(im0, persist=True, show=False,classes=0)
    tracks = model.track(im0, persist=True, show=False)
    # print(tracks.Boxes)
    counter.set_args(view_img=True,
                 reg_pts=region_points,
                 reg_pts_2=region_points_2,
                 classes_names=model.names,
                 draw_tracks=True)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()