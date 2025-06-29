# Portfolio Site

フリーランス Webデザイナー・ブロガーのポートフォリオサイト

## 概要

このサイトは Jekyll を使用して構築されており、GitHub Pages でホスティングされています。

## 機能

- **レスポンシブデザイン**: PC、タブレット、スマートフォンに対応
- **多言語対応**: 日本語・英語の2言語対応
- **作品ギャラリー**: 作品の追加・管理が容易
- **SEO最適化**: メタタグ、サイトマップ、構造化データ対応
- **高速読み込み**: 最適化されたコードとアセット

## 技術スタック

- Jekyll (静的サイトジェネレーター)
- HTML5 / CSS3 / JavaScript
- Sass (CSS前処理)
- GitHub Pages (ホスティング)

## セットアップ

1. リポジトリをクローン
```bash
git clone [repository-url]
cd portfolio-site
```

2. 依存関係をインストール
```bash
bundle install
```

3. ローカルサーバーを起動
```bash
bundle exec jekyll serve
```

4. ブラウザで http://localhost:4000 にアクセス

## 設定

### 基本設定
`_config.yml` で以下の設定を変更してください：

- `title`: サイトタイトル
- `email`: メールアドレス
- `description`: サイトの説明
- `twitter_username`: Twitterユーザー名
- `github_username`: GitHubユーザー名
- `google_analytics`: Google Analytics ID

### 作品の追加

1. `_works/` ディレクトリに新しいMarkdownファイルを作成
2. フロントマターで以下を設定：
   - `title`: 作品タイトル
   - `date`: 作成日
   - `category`: カテゴリ
   - `thumbnail`: サムネイル画像のパス
   - `technologies`: 使用技術（配列）
   - `url_link`: 作品のURL（オプション）

## デプロイ

GitHub Pages を使用してデプロイする場合：

1. GitHub にリポジトリをプッシュ
2. リポジトリの Settings > Pages でソースを設定
3. 自動的にサイトが公開されます

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。