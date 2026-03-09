# BookRecommendationSystem
A book recommendation system implemented using Python and flask based on machine learning and collaborative filtering algorithms
If you need to make the dataset public, please text me.These csv files can not be uplpad

## 项目简介
本书籍推荐系统是一个基于大数据分析与推荐算法的项目，旨在帮助用户快速找到适合他们阅读习惯和兴趣的书籍。本项目采用了高度模块化的前端和后端技术栈，使用 Python 和大数据框架开发推荐算法，并使用Flask前端框架。

---

## 主要功能
1. **用户书籍推荐**：
   - 通过聚类算法和用户行为数据进行协同过滤推荐。
   - 支持对用户兴趣的动态调整。

2. **前端与后端分离架构**：
   - 后端：基于 Flask 实现 API 服务。
   - 前端：采用 Bootstrap 和 Flat-UI，提供直观的界面。

3. **数据库支持**：
   - 使用公开.csv数据集导入数据库。
   - 使用 MySQL 作为项目的数据库，存储用户数据和书籍信息。
   
---

## 系统依赖
- **操作系统**：主开发环境推荐使用 Linux（如 CentOS 或 Ubuntu），也可以在 Windows 上运行。
- **后端框架与依赖**：
  - Python 3.7+
  - Flask
  - MySQL
- **推荐算法库**：
  - NumPy
  - pandas
  - scikit-learn
- **前端依赖**：
  - Bootstrap
  - Flat-UI

---

## 文件结构
以下是项目的关键文件和目录结构：

```plaintext
BookRecommendationSystem/
├── web/
│   ├── static/                # 前端静态文件
│   │   ├── bootstrap/         # Bootstrap 框架
│   │   ├── Flat-UI/           # Flat-UI 前端组件
│   │   ├── images/            # 图片资源
│   │   ├── css/               # 自定义 CSS 文件
│   │   └── js/                # 自定义 JS 文件
│   ├── templates/             # HTML 模板文件
│   └── app.py                 # Flask 主程序
├── config.py                  # 配置文件（数据库和系统配置）
├── requirements.txt           # Python 依赖列表
└── README.md                  # 项目说明文件
```
