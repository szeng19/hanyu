# 汉语新解

一个使用 AI 来重新解释汉语词语的 Web 应用。

## 功能特点

- 输入汉语词语获取 AI 解释
- 辛辣讽刺的解释风格
- 简洁直观的用户界面

## 安装说明

1. 克隆项目
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 创建 .env 文件并设置 OPENROUTER_API_KEY

## 运行方式

```bash
uvicorn app.main:app --reload
```

访问 http://localhost:8000 即可使用 新的内容
