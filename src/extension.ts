
import * as vscode from 'vscode';
import axios from 'axios';

const instance = axios.create({
	baseURL: 'http://127.0.0.1:30000',
	timeout: 10000
});


// 获取当前行代码
export function getLine(document: vscode.TextDocument, position: vscode.Position): string {
	let current_line: number = position.line;
	let current_row: number = position.character;
	console.log("Current line=" + current_line);
	console.log("Current row = " + current_row);

	let lines = document.lineCount;
	console.log("Lines:" + lines);

	let code: string = "";

	if (current_line < lines) {
		let codeLine = document.lineAt(current_line);
		code = codeLine.text;
	}
	console.log("code=" + code);
	return code;
}

export function activate(context: vscode.ExtensionContext) {

	let provider1 = vscode.languages.registerCompletionItemProvider('javascript', {

		async provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken, context: vscode.CompletionContext) {
			console.log('document version=' + document.version);
			console.log('text is:' + document.getText());
			console.log('URI is:' + document.uri);
			console.log('Language ID=' + document.languageId);
			console.log('Line Count=' + document.lineCount);

			let item: vscode.CompletionItem = await instance.post('/complete', { code: getLine(document, position) })
				.then(function (response: any) {
					console.log('complete: ' + response.data);
					return new vscode.CompletionItem(response.data);
				})
				.catch(function (error: Error) {
					console.log(error);
					return new vscode.CompletionItem('No suggestion');
				});

			return [item];

			/*
			// a simple completion item which inserts `Hello World!`
			const simpleCompletion = new vscode.CompletionItem('console.log');

			// a completion item that inserts its text as snippet,
			// the `insertText`-property is a `SnippetString` which will be
			// honored by the editor.
			const snippetCompletion = new vscode.CompletionItem('console');
			snippetCompletion.insertText = new vscode.SnippetString('console.${1|log,warn,error|}. Is it console.${1}?');
			snippetCompletion.documentation = new vscode.MarkdownString("Code snippet for console");

			// a completion item that can be accepted by a commit character,
			// the `commitCharacters`-property is set which means that the completion will
			// be inserted and then the character will be typed.
			const commitCharacterCompletion = new vscode.CompletionItem('console');
			commitCharacterCompletion.commitCharacters = ['.'];
			commitCharacterCompletion.documentation = new vscode.MarkdownString('Press `.` to get `console.`');

			// a completion item that retriggers IntelliSense when being accepted,
			// the `command`-property is set which the editor will execute after 
			// completion has been inserted. Also, the `insertText` is set so that 
			// a space is inserted after `new`
			const commandCompletion = new vscode.CompletionItem('new');
			commandCompletion.kind = vscode.CompletionItemKind.Keyword;
			commandCompletion.insertText = 'new ';
			commandCompletion.command = { command: 'editor.action.triggerSuggest', title: 'Re-trigger completions...' };

			// return all completion items as array
			return [
				simpleCompletion,
				snippetCompletion,
				commitCharacterCompletion,
				commandCompletion
			];*/

		}
	});

	/*
	const provider2 = vscode.languages.registerCompletionItemProvider(
		'plaintext',
		{
			provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {

				// get all text until the `position` and check if it reads `console.`
				// and if so then complete if `log`, `warn`, and `error`
				let linePrefix = document.lineAt(position).text.substr(0, position.character);
				if (!linePrefix.endsWith('console.')) {
					return undefined;
				}

				return [
					new vscode.CompletionItem('log', vscode.CompletionItemKind.Method),
					new vscode.CompletionItem('warn', vscode.CompletionItemKind.Method),
					new vscode.CompletionItem('error', vscode.CompletionItemKind.Method),
				];
			}
		},
		'.' // triggered whenever a '.' is being typed
	);

	context.subscriptions.push(provider1, provider2);*/
	context.subscriptions.push(provider1);
}