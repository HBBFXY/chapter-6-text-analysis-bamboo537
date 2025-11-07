# -*- 编码: utf-8 -*-

def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    参数：
        text - 输入的字符串
    返回：
        list - 按字符频率降序排列的字符列表（频率相同则按字符本身排序）
    """
    # 统计每个字符的出现频率
    frequency_dict = {}
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    # 按频率降序排序，频率相同时按字符升序排序
    sorted_char_items = sorted(frequency_dict.items(), key=lambda x: (-x[1], x[0]))
    # 提取排序后的字符列表
    return [char for char, count in sorted_char_items]


if __name__ == "__main__":
    print("文本字符频率分析器")
    print("=" * 30)
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    input_lines = []
    while True:
        try:
            current_line = input()
            if not current_line:  # 输入空行则终止输入
                break
            input_lines.append(current_line)
        except EOFError:
            break
    
    # 合并所有输入行（保留原始换行符）
    full_text = "\n".join(input_lines)
    
    # 处理无有效输入的情况
    if not full_text:
        print("未输入有效文本！")
    else:
        # 分析文本并获取排序后的字符
        result_chars = analyze_text(full_text)
        # 打印结果
        print("\n字符按频率降序排列：")
        print(", ".join(result_chars))
        print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
