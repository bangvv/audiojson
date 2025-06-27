import json

def merge_json_arrays(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    if not isinstance(data1, list) or not isinstance(data2, list):
        print("⚠️ Cả hai file JSON phải là mảng (list).")
        return

    merged = data1 + data2

    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(merged, out, ensure_ascii=False, indent=4)

    print(f"✅ Đã gộp xong vào file: {output_file}")

# Gọi hàm trực tiếp với tên file bạn yêu cầu
merge_json_arrays("temp.json", "_x.json", "vip.json")
