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
		//如果大于第2行，则取上一行一起做匹配
		if (current_line > 1) {
			const prevLine = document.lineAt(current_line - 1);
			code = prevLine.text + "\n" + code;
		}
	}
	console.log("code=" + code);
	return code;
}


//截掉最后一个.之前部分，避免补全时多补
export function getLastDot(compStr: string): string {
	const sections = compStr.split('.');
	let value = sections[sections.length - 1];
	//如果是以.结尾的，取倒数第二个，再把.补在后面
	if (value.length < 1) {
		value = sections[sections.length - 2] + ".";
	}
	return value;
}


//将最后一个后面不为空的"."前面的字符截取掉。
//因为补全的新信息中也可能有"."，所以先在源数据中做判断，取这部分的长度，再去补全结果中把前面这些部分去掉
export function processDot(origStr: string, compStr: string): string {
	const lastChar = origStr.charAt(origStr.length - 1);
	let noHeadStr: string;
	let pos: number;
	if (lastChar === '.') {
		//console.log('Last is .');
		let noDotStr = origStr.slice(0, origStr.length - 2);
		pos = noDotStr.lastIndexOf('.');

	} else {
		pos = origStr.lastIndexOf('.');
	}

	if (pos > 0) {
		noHeadStr = compStr.slice(pos + 1);
		//console.log(noHeadStr);
	} else {
		noHeadStr = compStr;
	}

	return noHeadStr;
}


export function processCompletion(compstr: string, origText: string): vscode.CompletionItem {
	console.log('complete: ' + compstr);
	const compLines = compstr.split('\n');
	let currentLine: string;
	if (compLines.length > 1) {
		currentLine = compLines[compLines.length - 1];
	} else {
		currentLine = compstr;
	}
	currentLine = currentLine.trim();
	origText = origText.trim();
	let aliOSItem = new vscode.CompletionItem(currentLine);
	//将最后一个后面不为空的"."前面的字符截取掉。
	//因为补全的新信息中也可能有"."，所以先在源数据中做判断，取这部分的长度，再去补全结果中把前面这些部分去掉

	aliOSItem.insertText = processDot(origText, currentLine);
	console.log('complete: ' + compstr);
	console.log(origText.length);
	console.log('insertText:' + aliOSItem.insertText);
	return aliOSItem;
}