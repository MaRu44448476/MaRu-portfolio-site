# プレビューガイド

このプロジェクトをローカルでプレビューする方法を説明します。

## 方法 1: Docker を使用 (推奨)

### 前提条件
- Docker がインストールされていること
- Docker Compose がインストールされていること

### 手順

1. **Docker でサイトを起動**
```bash
cd MaRu-portfolio-site
docker-compose up
```

2. **ブラウザでアクセス**
   - http://localhost:4000 でサイトが表示されます
   - ファイルを編集すると自動的にリロードされます

3. **停止**
```bash
docker-compose down
```

## 方法 2: 簡易プレビューサーバー

管理者権限がない環境での代替手段です。

### 使用方法

1. **プレビューサーバーを起動**
```bash
cd MaRu-portfolio-site
python3 preview_server.py
```

2. **ブラウザでアクセス**
   - http://localhost:8000 でサイト構造を確認できます
   - ⚠️ Jekyll の処理は行われないため、完全な表示はできません

3. **停止**
   - Ctrl+C でサーバーを停止

## 方法 3: Ruby/Jekyll を直接インストール

### Ubuntu/Debian の場合

```bash
# Ruby と依存関係をインストール
sudo apt update
sudo apt install ruby-full ruby-bundler build-essential

# プロジェクトディレクトリに移動
cd MaRu-portfolio-site

# Jekyll の依存関係をインストール
bundle install

# 開発サーバーを起動
bundle exec jekyll serve
```

### macOS の場合

```bash
# Homebrew で Ruby をインストール
brew install ruby

# プロジェクトディレクトリに移動
cd MaRu-portfolio-site

# Jekyll の依存関係をインストール
bundle install

# 開発サーバーを起動
bundle exec jekyll serve
```

### Windows の場合

1. **Ruby Installer をダウンロード**
   - https://rubyinstaller.org/ から最新版をダウンロード
   - インストール時に「MSYS2 development toolchain」を選択

2. **Jekyll をインストール**
```cmd
# コマンドプロンプトまたは PowerShell で実行
cd MaRu-portfolio-site
bundle install
bundle exec jekyll serve
```

## トラブルシューティング

### Docker でポートが使用中の場合

```bash
# 使用中のプロセスを確認
sudo lsof -i :4000

# ポートを変更してサーバーを起動
docker-compose run --rm -p 4001:4000 jekyll
```

### bundle install でエラーが発生する場合

```bash
# Ruby のバージョンを確認
ruby --version

# Ruby 2.7 以上が必要です
# 古いバージョンの場合は Ruby をアップデート
```

### 権限エラーが発生する場合

```bash
# Bundler のインストール先を変更
bundle config set --local path 'vendor/bundle'
bundle install
```

## 開発のヒント

### ファイル構造

- `_layouts/` - ページレイアウト
- `_includes/` - 共通パーツ
- `_sass/` - SCSS ファイル
- `_works/` - 作品データ
- `_data/` - サイト設定データ
- `assets/` - 静的ファイル

### 設定変更

- `_config.yml` - サイト全体の設定
- `_data/translations.yml` - 多言語対応テキスト
- `_data/navigation.yml` - ナビゲーション設定

### 作品追加

1. `_works/` ディレクトリに `.md` ファイルを作成
2. フロントマターで作品情報を設定
3. 作品画像を `assets/images/` に配置

## GitHub Pages でのデプロイ

1. **リポジトリを GitHub にプッシュ**
2. **Settings > Pages で GitHub Pages を有効化**
3. **Source を "Deploy from a branch" に設定**
4. **Branch を "main" に設定**
5. **自動的にサイトが公開されます**

URL: `https://yourusername.github.io/repository-name/`