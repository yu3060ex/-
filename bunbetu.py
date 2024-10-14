import os
import shutil

# 元のフォルダーとターゲットのフォルダーのパス
source_folder = r"ここにソース元のフォルダのパスを入れる"
destination_folder = r"移動先のフォルダを指定"

# 元のフォルダー内のファイルを処理
for file_name in os.listdir(source_folder):
    # ファイルのフルパスを取得
    file_path = os.path.join(source_folder, file_name)
    
    # ファイルかどうかを確認
    if os.path.isfile(file_path):
        # 拡張子を取得（拡張子は小文字に変換）
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # 拡張子に基づいてフォルダーを作成
        # フォルダー名がファイル名と重複しないように "_folder" を追加
        target_folder = os.path.join(destination_folder, file_extension.strip('.') + "_folder")
        os.makedirs(target_folder, exist_ok=True)
        
        # ファイルを新しいフォルダーに移動
        shutil.move(file_path, os.path.join(target_folder, file_name))

print("ファイルの分類が完了しました。")
