# RSS Reader

一个简洁的 RSS 阅读器，支持自动更新订阅源、评论和收藏功能。使用 GitHub Actions 自动抓取更新，GitHub Issues 作为评论系统，并通过 GitHub Pages 进行部署。

## 功能特点

- 🔄 每6小时自动更新 RSS 源
- 💬 使用 GitHub Issues 作为评论系统
- ⭐ 支持文章收藏功能
- 🌓 自动适配深色/浅色模式
- 📱 响应式设计，支持移动端
- 🔍 按时间分类展示文章
- 🎯 支持自定义 RSS 源

## 技术栈

- Python (feedparser) - RSS 解析
- GitHub Actions - 自动化部署
- GitHub Pages - 静态页面托管
- GitHub Issues - 评论系统
- HTML/CSS/JavaScript - 前端展示

## 快速开始

1. Fork 本仓库

2. 修改配置

编辑 `index.html` 中的 `GITHUB_REPO` 变量为你的仓库名：

```javascript
const GITHUB_REPO = '你的用户名/仓库名';
```

3. 添加 RSS 源

编辑 `feed.list` 文件，每行一个 RSS 源地址。

4. 本地测试

```bash
pip install -r requirements.txt
python fetch_feeds.py
python -m http.server 8000
```

5. 启用 GitHub Pages

在仓库设置中启用 GitHub Pages，选择 main 分支作为源。

## 自动更新

项目通过 GitHub Actions 实现自动更新：

- 每6小时自动运行一次
- 可以在 Actions 页面手动触发更新
- 更新后自动提交变更到仓库

## 自定义主题

编辑 `static/style.css` 文件中的 CSS 变量来自定义主题颜色：

```css
:root {
    --primary-color: #2c3e50;
    --bg-color: #f8f9fa;
    /* 其他颜色变量... */
}
```

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。