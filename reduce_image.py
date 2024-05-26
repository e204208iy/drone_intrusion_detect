import os

def delete_non_multiple_of_four(folder_path):
    # フォルダ内のファイルを取得
    files = os.listdir(folder_path)

    for file_name in files:
        # ファイルがPNGであり、"frame_"で始まり、".png"で終わるか確認
        if file_name.endswith(".png") and file_name.startswith("frame_"):
            # ファイル名から数字の部分を抽出
            number_str = file_name[len("frame_"):-len(".png")]

            try:
                # 数字に変換して4の倍数かどうかを判定
                number = int(number_str)
                if number % 10 != 0:
                    # 4の倍数でない場合はファイルを削除
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except ValueError:
                # 数字に変換できない場合は無視
                pass

if __name__ == "__main__":
    folder_path = "output_images"  # 画像が保存されているフォルダのパスを指定
    delete_non_multiple_of_four(folder_path)
