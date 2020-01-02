import json

code_result = {}

code_result['code1'] = 'happy'
code_result['code2'] = 'happyNew'
code_result['code3'] = 'happyNewYear'
code_result['status'] = 1

json_str = json.dumps(code_result)

print(json_str)
