#!/usr/bin/env python3
"""
Simple preview server for Jekyll site
Provides basic functionality to preview the site structure
"""

import http.server
import socketserver
import os
import json
from pathlib import Path

class JekyllPreviewHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Root redirect to index.html
        if self.path == '/':
            self.path = '/index.html'
        
        # Handle Jekyll-style URLs (without .html extension)
        elif not '.' in self.path.split('/')[-1]:
            html_path = self.path.rstrip('/') + '.html'
            if os.path.exists('.' + html_path):
                self.path = html_path
        
        # Serve static files
        return super().do_GET()
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def create_preview_index():
    """Create a simple preview index.html that doesn't require Jekyll processing"""
    preview_html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ポートフォリオサイト - プレビューモード</title>
    <link rel="stylesheet" href="/assets/css/main.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .notice { background: #fff3cd; border: 1px solid #ffeeba; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .preview-nav { background: #f8f9fa; padding: 20px 0; margin-bottom: 40px; }
        .preview-nav ul { list-style: none; padding: 0; display: flex; gap: 20px; justify-content: center; }
        .preview-nav a { text-decoration: none; color: #333; font-weight: 500; }
        .section { margin: 40px 0; }
        .works-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }
        .work-card { border: 1px solid #e0e0e0; padding: 20px; border-radius: 8px; }
        h1 { text-align: center; color: #333; }
        h2 { color: #555; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; }
    </style>
</head>
<body>
    <div class="preview-nav">
        <div class="container">
            <ul>
                <li><a href="/">ホーム</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/works.html">Works</a></li>
                <li><a href="/en/">English</a></li>
            </ul>
        </div>
    </div>
    
    <div class="container">
        <div class="notice">
            <strong>⚠️ プレビューモード</strong><br>
            これは Jekyll 処理なしの簡易プレビューです。完全な表示には Jekyll のインストールが必要です。
        </div>
        
        <h1>ポートフォリオサイト</h1>
        
        <div class="section">
            <h2>サイト構造</h2>
            <ul>
                <li><strong>ホーム</strong> - index.html</li>
                <li><strong>About</strong> - about.html</li>
                <li><strong>Works</strong> - works.html</li>
                <li><strong>英語版</strong> - /en/ ディレクトリ</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>作品一覧 (_works/)</h2>
            <div class="works-grid">
                <div class="work-card">
                    <h3>サンプルブログ</h3>
                    <p>_works/sample-blog.md</p>
                </div>
                <div class="work-card">
                    <h3>サンプルLP</h3>
                    <p>_works/sample-lp.md</p>
                </div>
                <div class="work-card">
                    <h3>サンプルWebデザイン</h3>
                    <p>_works/sample-web-design.md</p>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>Jekyll セットアップ手順</h2>
            <ol>
                <li>Ruby をインストール (sudo apt install ruby-full ruby-bundler)</li>
                <li>bundle install を実行</li>
                <li>bundle exec jekyll serve でサーバー起動</li>
            </ol>
        </div>
    </div>
    
    <script src="/assets/js/main.js"></script>
</body>
</html>"""
    
    with open('/home/wiwcw/MaRu-portfolio-site/preview_index.html', 'w', encoding='utf-8') as f:
        f.write(preview_html)
    print("✅ プレビュー用 index.html を作成しました")

def main():
    PORT = 8000
    
    # Create preview index
    create_preview_index()
    
    # Change to project directory
    os.chdir('/home/wiwcw/MaRu-portfolio-site')
    
    # Start server
    with socketserver.TCPServer(("", PORT), JekyllPreviewHandler) as httpd:
        print(f"""
╔════════════════════════════════════════════════════════════╗
║             Jekyll サイト プレビューサーバー                ║
╠════════════════════════════════════════════════════════════╣
║  🌐 URL: http://localhost:{PORT}                           ║
║  📁 ディレクトリ: /home/wiwcw/MaRu-portfolio-site         ║
║                                                            ║
║  ⚠️  注意: これは簡易プレビューです。                      ║
║     Jekyll の全機能を使うには、Ruby と Jekyll の          ║
║     インストールが必要です。                               ║
║                                                            ║
║  🛑 終了: Ctrl+C                                          ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✋ サーバーを停止しました")

if __name__ == "__main__":
    main()