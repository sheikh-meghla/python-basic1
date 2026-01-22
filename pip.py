import camelcase

# CamelCase তৈরি
c = camelcase.CamelCase()
txt = "hello world"
camel_txt = c.hump(txt)
print("CamelCase:", camel_txt)

# CamelCase → snake_case
def to_snake_case(text):
    import re
    # বড় অক্ষর এর আগে '_' বসিয়ে সব lowercase করা
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text

snake_txt = to_snake_case(camel_txt)
print("Snake Case:", snake_txt)

