#!/usr/bin/env python3
"""
电商价格监控脚本 - 演示版
功能：抓取指定商品的价格、销量、评价
注意：仅用于演示，不实际运行（需处理反爬）
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
from datetime import datetime

# 配置项
TARGET_URLS = [
    "https://item.taobao.com/item.htm?id=123456",  # 示例商品
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_product_info(url):
    """
    抓取商品信息
    Returns: dict with title, price, sales, rating
    """
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'html.parser')

        # 解析逻辑（示例，实际需根据页面结构）
        data = {
            'url': url,
            'title': '示例商品标题',
            'price': '99.00',
            'sales': '1000+',
            'rating': '4.8',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return data

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_to_excel(data_list, filename='prices.xlsx'):
    """保存到 Excel"""
    df = pd.DataFrame(data_list)
    df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

def send_alert(old_price, new_price, item):
    """价格变动提醒（示例）"""
    if float(new_price) < float(old_price) * 0.95:  # 降价5%以上
        print(f"[ALERT] {item['title']} price dropped from {old_price} to {new_price}")

def main():
    print("开始监控商品价格...")
    all_data = []

    for url in TARGET_URLS:
        data = fetch_product_info(url)
        if data:
            all_data.append(data)
            print(f"Fetched: {data['title']} - {data['price']}")

    if all_data:
        save_to_excel(all_data)

    print("监控完成")

if __name__ == "__main__":
    main()

---

## 使用说明

### 环境安装
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### 配置
1. 修改 `TARGET_URLS` 为你的商品链接
2. 根据需要调整解析逻辑

### 运行
```bash
python taobao-monitor.py
```

### 扩展功能
- 定时运行：crontab 或计划任务
- 微信推送：Server酱 或企业微信
- 数据库存储：MySQL/PostgreSQL
- 多线程：concurrent.futures

---

## 注意事项

⚠️ **本代码仅为演示框架**，实际部署需要：
1. 处理反爬（Selenium/Playwright）
2. 可能需要验证码识别
3. 遵守网站 terms of service
4. 不要频繁请求（建议每天1-2次）

---

## 定制服务

需要真实可用的监控脚本？  
联系：automation.openclaw@gmail.com  
价格：800-2000元（一次性）

---

#Python #自动化 #爬虫 #电商监控