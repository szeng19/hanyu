async function getExplanation() {
    const wordInput = document.getElementById('word-input');
    const resultDiv = document.getElementById('explanation-result');
    const word = wordInput.value.trim();

    if (!word) {
        alert('请输入要解释的词语');
        return;
    }

    resultDiv.innerHTML = '正在思考中...';

    try {
        const response = await fetch(`/api/explain?word=${encodeURIComponent(word)}`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (response.ok) {
            resultDiv.innerHTML = marked.parse(data.explanation);
        } else {
            resultDiv.innerHTML = `错误: ${data.detail}`;
        }
    } catch (error) {
        resultDiv.innerHTML = `发生错误: ${error.message}`;
    }
}

// 添加回车键处理函数
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        getExplanation();
    }
}

// 配置 marked 选项
marked.setOptions({
    breaks: true,  // 支持 GitHub 风格的换行
    gfm: true,     // 启用 GitHub 风格的 Markdown
    sanitize: false // 允许 HTML 标签
}); 