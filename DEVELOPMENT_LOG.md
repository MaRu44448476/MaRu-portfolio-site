# ポートフォリオサイト開発ログ

## プロジェクト概要

フリーランス Webデザイナー・ブロガーのポートフォリオサイトを Jekyll で構築しました。

### 完成したサイト
- **URL**: https://maru-vive.com
- **GitHub リポジトリ**: https://github.com/MaRu44448476/MaRu-portfolio-site

## 開発手順

### 1. 要件定義の確認
- `C:\Users\T.M\Downloads\portfolio-requirements.md` を元に仕様を決定
- GitHub Pages + Jekyll による静的サイト構築
- 多言語対応（日本語・英語）
- レスポンシブデザイン
- SEO対策

### 2. 技術スタック
- **静的サイトジェネレーター**: Jekyll
- **ホスティング**: GitHub Pages
- **スタイリング**: Sass/SCSS
- **多言語**: Jekyll データファイル
- **アニメーション**: CSS + JavaScript

### 3. 作成したファイル構成

```
/
├── _config.yml              # Jekyll設定
├── _data/
│   ├── navigation.yml       # ナビゲーション設定
│   └── translations.yml     # 多言語翻訳
├── _includes/
│   ├── header.html          # ヘッダーコンポーネント
│   └── footer.html          # フッターコンポーネント
├── _layouts/
│   ├── default.html         # ベースレイアウト
│   └── work.html            # 作品詳細レイアウト
├── _sass/
│   └── main.scss           # メインスタイル
├── _works/                  # 作品コレクション
│   ├── sample-web-design.md
│   ├── sample-lp.md
│   └── sample-blog.md
├── assets/
│   ├── css/main.scss       # CSS エントリーポイント
│   ├── js/main.js          # JavaScript
│   └── images/             # 画像ファイル
├── en/                     # 英語版ページ
│   ├── index.html
│   ├── about.html
│   └── works.html
├── index.html              # トップページ
├── about.html              # プロフィールページ
├── works.html              # 作品一覧ページ
├── CNAME                   # 独自ドメイン設定
└── robots.txt              # SEO設定
```

### 4. 実装した機能

#### 基本機能
- [x] ホームページ（自己紹介、サービス説明、作品プレビュー）
- [x] 作品ギャラリー（フィルタリング機能付き）
- [x] プロフィールページ
- [x] お問い合わせセクション（XのDMへ誘導）

#### 技術機能
- [x] レスポンシブデザイン（PC・タブレット・スマートフォン対応）
- [x] 多言語対応（日本語・英語切り替え）
- [x] SEO対策（メタタグ、サイトマップ、構造化データ）
- [x] Google Analytics 統合
- [x] GitHub Pages デプロイ設定

#### UX/UI
- [x] ミニマルデザイン
- [x] スクロールアニメーション
- [x] モバイルメニュー
- [x] 直感的なナビゲーション

### 5. 設定項目

#### 完了済み設定
- **Twitter**: @Maru44448476
- **Email**: tkmr.3aeau@gmail.com
- **Google Analytics ID**: G-NZRXQQ8WSZ
- **独自ドメイン**: maru-vive.com
- **プロフィール画像**: 実際の画像に変更済み

#### DNS設定（要実施）
```
Aレコード:
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

CNAMEレコード:
www → maru44448476.github.io
```

### 6. トラブルシューティング履歴

#### 問題1: 404エラー
- **原因**: ファイルが `portfolio-site/` サブディレクトリにあった
- **解決**: ルートディレクトリにファイルを移動

#### 問題2: GitHub プッシュエラー
- **原因**: 大きなファイル（Next.js関連）が含まれていた
- **解決**: Jekyllファイルのみで新しいリポジトリを作成

#### 問題3: 認証エラー
- **原因**: Personal Access Token が未設定
- **解決**: GitHub で PAT を作成して使用

### 7. 今後のメンテナンス

#### 定期的な作業
- **月次**: Google Analytics レポート確認
- **四半期**: 依存関係の更新
- **随時**: 作品の追加・更新

#### 作品追加手順
1. `_works/` ディレクトリに新しい `.md` ファイルを作成
2. フロントマターで作品情報を設定
3. 作品画像を `assets/images/` に配置
4. Git にコミット・プッシュ

### 8. 参考情報

- **Jekyll ドキュメント**: https://jekyllrb.com/docs/
- **GitHub Pages ガイド**: https://docs.github.com/pages
- **設定ガイド**: SETUP_GUIDE.md を参照

---

**開発期間**: 2025年6月29日  
**開発者**: Claude Code + MaRu44448476  
**最終更新**: 2025年6月29日