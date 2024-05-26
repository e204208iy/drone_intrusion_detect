import cv2
import os

def video_to_images(video_path, output_folder, target_fps):
    # ビデオキャプチャの作成
    cap = cv2.VideoCapture(video_path)

    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # フレームレートの取得
    original_fps = cap.get(cv2.CAP_PROP_FPS)

    # 新しいフレームレートを計算
    new_fps = original_fps / target_fps

    # フレームの取得
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # 画像の保存
        image_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(image_path, frame)

        frame_count += 1

        # 一定の時間待機してフレームレートを調整
        delay = int(1000 / new_fps)
        cv2.waitKey(delay)

    # キャプチャの解放
    cap.release()

if __name__ == "__main__":
    video_path = "videos/haruta.mp4"  # 入力となる動画ファイルのパスを指定
    output_folder = "output_images"  # 画像を保存するフォルダのパスを指定
    target_fps = 1  # 新しいフレームレートを指定

    video_to_images(video_path, output_folder, target_fps)
