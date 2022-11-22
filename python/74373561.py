import json

string = '{"key1":"my"value","key2":"my"value2"}'
js = json.loads(string, strict=False)
pass

# The variable `string` is not a valid JSON string.
# The correct string should be:
# '{"key1":"my\\"value","key2":"my\\"value2"}'