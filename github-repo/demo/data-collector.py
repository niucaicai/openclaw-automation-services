#!/usr/bin/env python3
"""
通用数据采集器 - 演示版
功能：从指定网站采集结构化数据
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime

# 示例：采集新闻网站
TARGET_URL = "https://news.example.com"  # 替换为目标网站

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_news_articles(url):
    """采集新闻文章（示例）"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'html.parser')

        # 这里需要根据实际网站结构调整选择器
        articles = []
        for item in soup.select('.article-item'):  # 示例选择器
            title = item.select_one('.title').text.strip()
            link = item.select_one('a')['href']
            date = item.select_one('.date').text.strip()

            articles.append({
                'title': title,
                'link': link,
                'date': date,
                'collected_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        return articles

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def save_json(data, filename='news.json'):
    """保存为 JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved JSON: {filename}")

def save_excel(data, filename='news.xlsx'):
    """保存为 Excel"""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Saved Excel: {filename}")

def main():
    print("开始采集数据...")
    articles = fetch_news_articles(TARGET_URL)

    if articles:
        print(f"采集到 {len(articles)} 条文章")
        save_json(articles)
        save_excel(articles)
    else:
        print("未采集到数据")

if __name__ == "__main__":
    main()

---

## 使用说明

### 安装
```bash
pip install requests beautifulsoup4 pandas
```

### 配置
1. 修改 `TARGET_URL` 为目标网站
2. 调整 `fetch_news_articles` 中的选择器（CSS Selector）以匹配目标网站结构
3. 如需翻页，添加循环逻辑

### 运行
```bash
python data-collector.py
```

### 常见配置

**采集文章标题和链接**：
```python
for item in soup.select('.post-item'):
    title = item.select_one('h2 a').text.strip()
    link = item.select_one('h2 a')['href']
```

**采集分页**：
```python
for page in range(1, 6):  # 前5页
    url = f"{TARGET_URL}/page/{page}"
    # 抓取逻辑...
```

**延迟请求**（避免被封）：
```python
import random
time.sleep(random.uniform(1, 3))  # 1-3秒随机延迟
```

---

## 扩展功能

- **增量采集**：记录已采集URL，避免重复
- **代理支持**：使用代理池
- **验证码处理**：接入打码平台
- **数据清洗**：去重、格式化、翻译
- **自动推送**：结果发送到微信/邮件

---

## 合规提醒

⚠️ 使用本脚本前请确认：
1. 目标网站允许爬虫（检查 robots.txt）
2. 不采集个人隐私或敏感信息
3. 控制请求频率，不给目标服务器造成压力
4. 遵守网站服务条款

---

## 定制服务

需要针对特定网站定制爬虫？  
联系：automation.openclaw@gmail.com  
价格：500-2000元（根据复杂度）

---

#Python #爬虫 #数据采集 #自动化