# -*- 编码: utf-8 -*-

def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    参数：text - 输入的字符串
    返回：按频率降序排列的 (字符, 频率) 元组列表
    """
    # 统计字符频率（包含所有字符，无过滤）
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    # 按频率降序、字符升序排序
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items  # 返回 (字符, 频率) 元组列表


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
    
    if not full_text:
        print("未输入有效文本！")
    else:
        # 获取 (字符, 频率) 列表
        sorted_char_freq = analyze_text(full_text)
        # 提取字符列表（匹配原需求的输出格式）
        sorted_chars = [char for char, count in sorted_char_freq]
        
        print("\n字符按频率降序排列：")
        print(", ".join(sorted_chars))
        print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
