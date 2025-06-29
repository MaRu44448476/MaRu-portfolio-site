# ポートフォリオサイト セットアップガイド

## 1. Google Analytics の設定

### Google Analytics IDの取得方法

1. **Google Analytics にアクセス**
   - https://analytics.google.com/ にアクセス
   - Googleアカウントでログイン

2. **新しいプロパティの作成**
   - 「測定を開始」をクリック
   - アカウント名を入力（例：「ポートフォリオサイト」）
   - プロパティ名を入力（例：「portfolio-site」）
   - タイムゾーンを「日本」に設定
   - 通貨を「日本円」に設定

3. **データストリームの設定**
   - 「ウェブ」を選択
   - ウェブサイトのURL を入力（例：`https://yourdomain.com`）
   - ストリーム名を入力

4. **測定IDの取得**
   - 作成後、「G-XXXXXXXXXX」形式のIDが表示されます
   - このIDを `_config.yml` の `google_analytics` に設定

### _config.yml での設定例
```yaml
google_analytics: G-XXXXXXXXXX
```

## 2. ドメイン設定（GitHub Pages）

### 独自ドメインの取得

1. **ドメイン登録サービスで購入**
   - お名前.com、ムームードメイン、Google Domains など
   - 年間 1,000〜3,000円程度

2. **おすすめのドメイン例**
   - `yourname-portfolio.com`
   - `yourname.dev`
   - `yourname-design.com`

### GitHub Pages での独自ドメイン設定

#### 方法1: GitHubの管理画面から設定

1. **リポジトリの Settings へ**
   - GitHubのリポジトリページで「Settings」タブをクリック

2. **Pages 設定を開く**
   - 左メニューから「Pages」を選択

3. **Custom domain を設定**
   - 「Custom domain」欄に独自ドメインを入力
   - 例：`portfolio.example.com`
   - 「Save」をクリック

#### 方法2: CNAMEファイルで設定

1. **CNAMEファイルを作成**
```bash
echo "portfolio.example.com" > CNAME
```

2. **リポジトリにコミット・プッシュ**
```bash
git add CNAME
git commit -m "Add custom domain"
git push origin main
```

### DNS設定

ドメイン登録サービスで以下のDNS設定を行います：

#### Aレコード設定（ルートドメインの場合）
```
Type: A
Name: @
Value: 185.199.108.153
       185.199.109.153
       185.199.110.153
       185.199.111.153
```

#### CNAMEレコード設定（サブドメインの場合）
```
Type: CNAME
Name: portfolio（またはwww）
Value: yourusername.github.io
```

### SSL証明書の有効化

1. **DNS設定が反映されるまで待機**（最大24-48時間）

2. **GitHub Pages の設定で SSL を有効化**
   - リポジトリの Settings > Pages
   - 「Enforce HTTPS」にチェックを入れる

## 3. サイトの確認とテスト

### ローカルでの確認
```bash
# 依存関係のインストール
bundle install

# ローカルサーバーの起動
bundle exec jekyll serve

# ブラウザで確認
# http://localhost:4000
```

### デプロイ後の確認項目

- [ ] 独自ドメインでアクセスできる
- [ ] HTTPSが有効になっている
- [ ] 全ページが正常に表示される
- [ ] レスポンシブデザインが機能している
- [ ] 多言語切り替えが動作している
- [ ] Google Analytics でアクセスが計測されている

## 4. 継続的な運用

### 作品の追加方法

1. **`_works/` ディレクトリに新しいファイルを作成**
```markdown
---
layout: work
title: "新しい作品"
date: 2024-XX-XX
category: "Webデザイン"
thumbnail: "/assets/images/work-thumbnail.jpg"
technologies:
  - HTML5
  - CSS3
  - JavaScript
---

作品の説明をここに書きます。
```

2. **作品画像をアップロード**
   - `assets/images/` ディレクトリに画像を配置

3. **GitHubにプッシュ**
```bash
git add .
git commit -m "Add new work: 新しい作品"
git push origin main
```

### 定期メンテナンス

- **月次**: Google Analytics のアクセス状況確認
- **四半期**: 依存関係のアップデート
- **年次**: ドメインの更新

## トラブルシューティング

### よくある問題と解決方法

1. **サイトが表示されない**
   - DNS設定を確認
   - CNAMEファイルの内容を確認
   - GitHub Pages の設定を確認

2. **Google Analytics が動作しない**
   - 測定IDが正しく設定されているか確認
   - ブラウザの広告ブロッカーを無効化してテスト

3. **画像が表示されない**
   - 画像のパスが正しいか確認
   - 画像ファイルがリポジトリにアップロードされているか確認

## サポート

何か問題が発生した場合は、以下を確認してください：

1. GitHub Pages のステータス: https://www.githubstatus.com/
2. Jekyll のドキュメント: https://jekyllrb.com/docs/
3. このリポジトリの Issues セクション