##test
import os

def read_and_print_file(filename):
    """讀取並輸出檔案內容"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')  # end='' 避免多餘的換行
    except FileNotFoundError:
        print(f"找不到檔案：{filename}")
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")

if __name__ == "__main__":
    filename = "找找自己問題.txt"
    if os.path.exists(filename): #檢查檔案是否存在。
      read_and_print_file(filename)
    else:
      print(f"檔案 {filename} 不存在於當前目錄。")
