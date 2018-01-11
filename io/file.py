import sys
import os


def touch_new_file(file_name, content):
    """输出字符到新文件中.

    Args:
        file_name: filename.
        content: file content.

    Returns:
        None.

    Examples:
        >>> filename = 'testfile'
        >>> content = 'Old soldiers never die. They just fade away.'
        >>> touch_new_file(filename, content)
    """
    d_file = open(file_name, 'w')
    d_file.writelines(content)
    d_file.close()


def replace_string_in_file(file_path, old_str, new_str, new_file_name=None):
    """替换文件中的字符

    Returns:
        None.

    Examples:
        >>> filename = 'testfile'
        >>> content = 'Old soldiers never die. They just fade away.'
        >>> touch_new_file(filename, content)
        >>> replace_string_in_file(filename, "soldiers", "programmers")
    """
    if not os.path.isfile(file_path):
        print('No such file.')
        sys.exit()

    s_file = open(file_path, 'r+')
    d_file = open(file_path + '.tmp', 'w')

    for line in s_file.readlines():
        d_file.writelines(line.replace(old_str, new_str))
    s_file.close()
    d_file.close()

    if new_file_name:
        os.rename(file_path + '.tmp', new_file_name)
    else:
        os.remove(file_path)
        os.rename(file_path + '.tmp', file_path)

if __name__ == '__main__':
    pass
