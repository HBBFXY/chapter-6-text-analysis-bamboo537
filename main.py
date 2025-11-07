# -*- 编码: utf-8 -*-

def analyze_text(text):
    """
    分析文本中字母字符的频率并按频率降序排列
    参数：text - 输入的字符串
    返回：按频率降序排列的字母字符列表（仅包含字母）
    """
    # 仅统计字母字符（忽略非字母）
    freq = {}
    for char in text:
        if char.isalpha():  # 只保留字母
            freq[char] = freq.get(char, 0) + 1
    
    # 按频率降序、字母升序排序
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    # 返回字母列表
    return [char for char, count in sorted_items]


if __name__ == "__main__":
    print("文本字符频率分析器")
    print("=" * 30)
    print("请输入一段文本（输入空行结束）：")
    
    input_lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            input_lines.append(line)
        except EOFError:
            break
    
    full_text = "\n".join(input_lines)
    sorted_letters = analyze_text(full_text)
    
    if not sorted_letters:
        print("未输入有效字母！")
    else:
        print("\n字母按频率降序排列：")
        print(", ".join(sorted_letters))
        print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
