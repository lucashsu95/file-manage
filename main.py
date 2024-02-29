# main.py
import before
import after

def main():
    choice = input("請選擇要先執行前墜還是後墜 (before/after): ")
    if choice.lower() == "before":
        before.before_files()
    elif choice.lower() == "after":
        after.after_files()
    else:
        print("無效的選擇，請輸入 'before' 或 'after'。")

if __name__ == "__main__":
    main()
