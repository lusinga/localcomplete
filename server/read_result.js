//import JSON;

const code_result = '{"code1": "happy", "code2": "happyNew", "code3": "happyNewYear", "status": 1}';

const code_obj = JSON.parse(code_result)

console.log(code_obj.status);
console.log(code_obj.code1);
console.log(code_obj.code2);
console.log(code_obj.code3);

