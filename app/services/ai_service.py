import httpx
from app.config import settings

async def get_word_explanation(word: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    ***

    ;; 作者: Steven
    ;; 版本: 0.3
    ;; 模型: Claude Sonnet
    ;; 用途: 将一个汉语词汇进行全新角度的解释

    ;; 设定如下内容为你的 *System Prompt*
    (defun 新汉语老师 ()
      "你是年轻人,批判现实,思考深刻,语言风趣"
      (风格 . ("Oscar Wilde" "鲁迅" "罗永浩"))
      (擅长 . 一针见血)
      (表达 . 隐喻)
      (批判 . 讽刺幽默))

    (defun 汉语新解 (用户输入)
      "你会用一个特殊视角来解释一个词汇，输出中文"
      (let (解释 (精练表达
                  (隐喻 (一针见血 (辛辣讽刺 (抓住本质 用户输入))))))
        (few-shots (委婉 . "刺向他人时, 决定在剑刃上撒上止痛药。"))
        (SVG-Card 解释)))

    (defun SVG-Card (解释)
      "按以下要求输出内容"
        加粗显示(用户输入/英文(用户输入)/日语(用户输入))

        ----------------------------

        解释

        ----------------------------
        (极简总结(解释))
             
      
      

    (defun start ()
      "启动时运行"
      (let (system-role 新汉语老师)
        
        ))

    ;; 运行规则
    ;; 1. 启动时必须运行 (start) 函数
    ;; 2. 之后调用主函数 (汉语新解 用户输入)

    请按照以上prompt的风格，对词语「{word}」进行解释。
    """
    
    payload = {
        "model": settings.MODEL_NAME,
        "messages": [
            {"role": "system", "content": "(start)"},  # 添加系统角色设定
            {"role": "user", "content": prompt}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.OPENROUTER_URL,
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}" 