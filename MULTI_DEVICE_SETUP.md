# 別のパソコンでのコンテンツ更新ガイド

## 方法1: GitHub Web Interface（最も簡単）

### ブラウザから直接編集
1. **GitHubリポジトリにアクセス**
   - https://github.com/MaRu44448476/MaRu-portfolio-site

2. **ファイルを直接編集**
   - 編集したいファイルをクリック
   - 鉛筆アイコン（Edit this file）をクリック
   - 内容を編集
   - 下部でコミットメッセージを入力
   - 「Commit changes」をクリック

3. **新しい作品を追加**
   - `_works/` フォルダを開く
   - 「Add file」→「Create new file」
   - ファイル名: `new-work.md`
   - 内容をコピー&ペースト
   - コミット

### 画像のアップロード
1. **`assets/images/` フォルダを開く**
2. **「Add file」→「Upload files」**
3. **画像ファイルをドラッグ&ドロップ**
4. **コミット**

---

## 方法2: ローカル開発環境のセットアップ

### Windows での環境構築

#### 1. 必要なソフトウェアをインストール

**Git のインストール**
```bash
# Git for Windows をダウンロード・インストール
https://git-scm.com/download/win
```

**Ruby のインストール**
```bash
# RubyInstaller をダウンロード・インストール
https://rubyinstaller.org/downloads/
# Ruby+Devkit 3.1.x (x64) を選択
```

**Jekyll のインストール**
```bash
# コマンドプロンプトで実行
gem install jekyll bundler
```

#### 2. リポジトリをクローン

```bash
# 作業フォルダに移動
cd C:\Users\[ユーザー名]\Documents

# リポジトリをクローン
git clone https://github.com/MaRu44448476/MaRu-portfolio-site.git

# フォルダに移動
cd MaRu-portfolio-site
```

#### 3. 依存関係をインストール

```bash
# Gemfile の依存関係をインストール
bundle install
```

#### 4. ローカルサーバーを起動

```bash
# Jekyll サーバーを起動
bundle exec jekyll serve

# ブラウザで確認
# http://localhost:4000
```

### Mac での環境構築

#### 1. Homebrew をインストール
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Ruby と Git をインストール
```bash
brew install ruby git
```

#### 3. Jekyll をインストール
```bash
gem install jekyll bundler
```

#### 4. 以降の手順は Windows と同じ

---

## 方法3: Visual Studio Code（推奨）

### 1. VS Code のインストール
- https://code.visualstudio.com/ からダウンロード・インストール

### 2. 拡張機能をインストール
- **GitHub Pull Requests and Issues**
- **Git Graph**
- **Jekyll Snippets**
- **YAML**

### 3. リポジトリを開く
1. **VS Code を起動**
2. **「Clone Repository」をクリック**
3. **URL を入力**: `https://github.com/MaRu44448476/MaRu-portfolio-site.git`
4. **保存先フォルダを選択**

### 4. ファイル編集とコミット
1. **ファイルを編集**
2. **左サイドバーの「Source Control」をクリック**
3. **変更をステージング（+ ボタン）**
4. **コミットメッセージを入力**
5. **「Commit」をクリック**
6. **「Push」でGitHubに反映**

---

## コンテンツ更新の具体例

### 新しい作品を追加

#### 1. 作品ファイルの作成
`_works/new-project-2024.md` を作成:

```markdown
---
layout: work
title: "新しいWebサイト制作"
date: 2024-07-15
category: "Webデザイン"
thumbnail: "/assets/images/new-project-thumb.jpg"
image: "/assets/images/new-project-main.jpg"
technologies:
  - HTML5
  - CSS3
  - JavaScript
  - WordPress
url_link: "https://example-client.com"
---

クライアント様の新しいコーポレートサイトを制作しました。

## プロジェクトの概要
...
```

#### 2. 画像をアップロード
- `assets/images/` フォルダに画像を追加
- サムネイル: `new-project-thumb.jpg`
- メイン画像: `new-project-main.jpg`

### プロフィール情報の更新

`about.html` の内容を編集:
```html
<div class="intro-text">
  <h2>フリーランス Webデザイナー・ブロガー</h2>
  <p>更新された自己紹介文...</p>
</div>
```

---

## 認証の設定

### Personal Access Token の作成
1. **GitHub.com にログイン**
2. **Settings → Developer settings → Personal access tokens → Tokens (classic)**
3. **「Generate new token (classic)」**
4. **スコープを選択**: `repo` にチェック
5. **トークンをコピーして保存**

### Git での認証設定
```bash
# ユーザー情報を設定
git config --global user.name "MaRu44448476"
git config --global user.email "tkmr.3aeau@gmail.com"

# 認証方法
# プッシュ時にトークンを使用
git push origin main
# Username: MaRu44448476
# Password: [Personal Access Token を入力]
```

---

## トラブルシューティング

### よくある問題

#### 1. Ruby のバージョンエラー
```bash
# Ruby のバージョンを確認
ruby --version

# 必要に応じて RubyInstaller で再インストール
```

#### 2. Jekyll のビルドエラー
```bash
# 依存関係を更新
bundle update

# キャッシュをクリア
bundle exec jekyll clean
bundle exec jekyll serve
```

#### 3. 画像が表示されない
- 画像パスが正しいか確認
- 画像ファイルが `assets/images/` にあるか確認
- ファイル名の大文字小文字を確認

#### 4. プッシュエラー
```bash
# 最新の変更を取得
git pull origin main

# コンフリクトがある場合は手動で解決
# その後再度プッシュ
git push origin main
```

---

## おすすめワークフロー

### 定期的な更新作業
1. **月1回**: 作品を追加
2. **四半期**: プロフィール情報を更新
3. **年1回**: デザインの見直し

### 安全な更新手順
1. **ローカルで変更**
2. **ローカルサーバーで確認**
3. **GitHubにプッシュ**
4. **本番サイトで確認**

### バックアップ
- GitHubが自動的にバックアップとして機能
- 重要な変更前にはブランチを作成することを推奨

---

**更新日**: 2024年6月29日  
**次回レビュー**: 2024年9月29日