import React, { useCallback, useEffect, useState } from 'react';
import Editor, { loader, OnMount } from '@monaco-editor/react';
import type { editor as MonacoEditor } from 'monaco-editor';

const cdn = 'https://cdn.bootcdn.net/ajax/libs/monaco-editor/0.52.0/min/vs';
loader.config({ paths: { 'vs': cdn }})

interface SkillEditorProps {
  value: object; // 输入值必须是 object 类型
  onChange: (value: object) => void; // 返回解析后的 object
  onError: (message: string | null) => void; // 错误回调
}

export const skillPlaceholder = `{
  "function": {
    "name": "My Skill",
    "description": "This is a sample skill definition.",
    "parameters": {
        "properties": {
          "id":{ "description": "The ID of the skill.",  "type": "string"}
        }
    }
  },
  "url": "http://localhostt:8000/api/v1/skills/my-skill"
}`

const SkillEditor: React.FC<SkillEditorProps> = ({ value, onChange, onError }) => {
  const [editor, setEditor] = useState<MonacoEditor.IStandaloneCodeEditor | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleEditorDidMount: OnMount = useCallback((editor: MonacoEditor.IStandaloneCodeEditor) => {
    setEditor(editor);
  }, []);

  const handleEditorChange = useCallback(
    (value: string | undefined) => {
      try {
        // 解析输入的 JSON 字符串
        const parsedValue = JSON.parse(value || '{}');
        // 确保解析后的值是 object 类型
        if (typeof parsedValue === 'object' && !Array.isArray(parsedValue)) {
          onChange(parsedValue); // 返回 object
          setErrorMessage(null);
          onError(null);
        } else {
          throw new Error('Input must be a valid JSON object.');
        }
      } catch (error) {
        const message = error instanceof Error ? error.message : 'Invalid JSON';
        setErrorMessage(message);
        onError(message);
      }
    },
    [onChange, onError]
  );

  useEffect(() => {
    if (editor) {
      const model = editor.getModel();
      if (model) {
        model.updateOptions({ tabSize: 2 });
      }
    }
  }, [editor]);

  return (
    <div>
      <Editor
        height="300px"
        defaultLanguage="json" // 设置为 JSON 编辑器
        defaultValue={value || skillPlaceholder}
        onChange={handleEditorChange}
        onMount={handleEditorDidMount}
        options={{
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          fontSize: 14,
          lineNumbers: 'on',
          roundedSelection: false,
          scrollbar: {
            vertical: 'auto',
            horizontal: 'auto',
          },
          tabSize: 2,
        }}
      />
      {errorMessage && <div style={{ color: 'red', marginTop: '10px' }}>{errorMessage}</div>}
    </div>
  );
};

export default SkillEditor;