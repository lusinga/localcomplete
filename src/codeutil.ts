import * as vscode from 'vscode';


// 获取当前行代码
export function getLine(document: vscode.TextDocument, position: vscode.Position): string {
	let current_line: number = position.line;
	let current_row: number = position.character;
	//console.log("Current line=" + current_line);
	//console.log("Current row = " + current_row);

	let lines = document.lineCount;
	//console.log("Lines:" + lines);

	let code: string = "";

	if (current_line < lines) {
		let codeLine = document.lineAt(current_line);
		code = codeLine.text;
	}
	console.log("code=" + code);
	return code;
}


//截掉最后一个.之后部分，避免补全时多补
export function getLastDot(compStr: string): string {
	const sections = compStr.split('.');
	let value = sections[sections.length - 1];
	//如果是以.结尾的，取倒数第二个，再把.补在后面
	if (value.length < 1) {
		value = sections[sections.length - 2]+".";
	}
	return value;
}