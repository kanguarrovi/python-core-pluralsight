def tag(name, **attributes):
    print(attributes)
    result = '<' + name
    for key, value in attributes.items():
        result += f' {key}="{str(value)}"'
    result += '>'
    return result


if __name__ == '__main__':
    print(tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1))

