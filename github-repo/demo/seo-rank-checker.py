#!/usr/bin/env python3
"""
SEO 关键词排名追踪脚本 - 演示版
功能：查询指定关键词在搜索引擎的排名
注意：仅演示，实际需处理反爬和代理
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

# 配置
KEYWORDS = [
    "Python自动化",
    "电商运营",
    "SEO优化",
]

SEARCH_ENGINES = {
    "baidu": "https://www.baidu.com/s?wd={}",
    "google": "https://www.google.com/search?q={}",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_rank(keyword, engine="baidu"):
    """获取关键词排名（演示版）"""
    url = SEARCH_ENGINES[engine].format(keyword)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'html.parser')

        # 模拟：实际需要解析搜索结果
        # 这里返回随机数演示
        import random
        rank = random.randint(1, 100)

        return {
            'keyword': keyword,
            'engine': engine,
            'rank': rank,
            'url': url,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

    except Exception as e:
        print(f"Error: {e}")
        return None

def save_report(data, filename='seo-report.xlsx'):
    """保存报告"""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Report saved: {filename}")

def main():
    print("开始追踪关键词排名...")
    results = []

    for keyword in KEYWORDS:
        for engine in SEARCH_ENGINES.keys():
            rank_data = get_rank(keyword, engine)
            if rank_data:
                results.append(rank_data)
                print(f"{keyword} on {engine}: rank {rank_data['rank']}")
            time.sleep(1)  # 避免请求过快

    if results:
        save_report(results)

    print("追踪完成")

if __name__ == "__main__":
    main()

---

## 使用说明

### 安装
```bash
pip install requests beautifulsoup4 pandas
```

### 配置
1. 在 `KEYWORDS` 列表中添加你的关键词
2. 在 `SEARCH_ENGINES` 中选择搜索引擎
3. 修改 `get_rank` 函数的解析逻辑（根据实际页面结构）

### 运行
```bash
python seo-rank-checker.py
```

### 实际部署注意事项
- 需要代理IP池（避免被封）
- 可能需要处理验证码
- 建议每天查询1-2次
- 存储历史数据做趋势分析

---

## 定制服务

需要真实的 SEO 监控系统？  
联系：automation.openclaw@gmail.com  
价格：800元/月（包含50个关键词）

---

#Python #SEO #自动化 #排名追踪