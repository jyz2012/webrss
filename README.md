# RSS reader

- 使用 Python 抓取 RSS 文章
- 参考 hackernews 的实现模式
- 使用 GitHub Issues 作为评论系统
- 使用 GitHub Actions 自动更新 RSS 源
- 使用 GitHub Pages 部署

# Deploy

```bash
pip install -r requirements.txt
python fetch_rss.py
python -m http.server 8000
```