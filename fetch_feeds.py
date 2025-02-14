import feedparser
import re
import json
from datetime import datetime
import pytz
from collections import defaultdict

def fetch_feeds():
    with open('feed.list', 'r') as f:
        feeds = f.read().splitlines()
    
    articles_by_source = defaultdict(list)
    all_articles = []
    
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                published = entry.get('published_parsed', entry.get('updated_parsed'))
                if published:
                    dt = datetime(*published[:6])
                    dt = pytz.UTC.localize(dt)
                    beijing_tz = pytz.timezone('Asia/Shanghai')
                    dt = dt.astimezone(beijing_tz)
                    published_str = dt.strftime('%Y-%m-%d %H:%M')
                else:
                    published_str = ''
                
                summary = ''
                if 'summary' in entry:
                    summary = re.sub(r'<[^>]+>', '', entry.summary)
                    summary = summary.strip()[:150] + ('...' if len(summary) > 150 else '')
                elif 'description' in entry:
                    summary = re.sub(r'<[^>]+>', '', entry.description)
                    summary = summary.strip()[:150] + ('...' if len(summary) > 150 else '')
                
                article = {
                    'title': entry.title,
                    'link': entry.link,
                    'date': published_str,
                    'author': feed.feed.title,
                    'timestamp': dt.timestamp() if published else 0,
                    'summary': summary or '无摘要',
                    'source_url': feed.feed.link or feed_url
                }
                articles_by_source[feed.feed.title].append(article)
                all_articles.append(article)
        except Exception as e:
            print(f"Error fetching {feed_url}: {str(e)}")
            continue
    
    # 获取每个源最新的一篇文章
    latest_articles = []
    for source_articles in articles_by_source.values():
        if source_articles:
            latest = max(source_articles, key=lambda x: x['timestamp'])
            latest_articles.append(latest)
    
    # 如果文章数量不足50，从所有文章中取最新的补充
    if len(latest_articles) < 50:
        all_articles.sort(key=lambda x: x['timestamp'], reverse=True)
        latest_articles = list({article['link']: article for article in (latest_articles + all_articles[:50])}.values())
    
    # 最终按时间排序
    latest_articles.sort(key=lambda x: x['timestamp'], reverse=True)
    latest_articles = latest_articles[:50]
    
    # 保存为JSON文件
    data = {
        'update_time': datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M'),
        'articles': latest_articles
    }
    
    with open('feed.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fetch_feeds() 