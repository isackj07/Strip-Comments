def strip_comments(input_str, markers):
    lines = input_str.split('\n')
    output_lines = []
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)]
        output_lines.append(line.rstrip())
    return '\n'.join(output_lines)
    pass
