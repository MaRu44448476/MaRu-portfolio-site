#!/bin/bash

# バージョン更新スクリプト
# 使用方法: ./version-update.sh [major|minor|patch]

set -e

# 引数チェック
if [ $# -eq 0 ]; then
    echo "使用方法: $0 [major|minor|patch]"
    echo "例: $0 patch  # 1.0.0 → 1.0.1"
    echo "例: $0 minor  # 1.0.1 → 1.1.0"
    echo "例: $0 major  # 1.1.0 → 2.0.0"
    exit 1
fi

# 現在のバージョンを取得
current_version=$(grep "version:" _config.yml | sed 's/version: "//' | sed 's/"//')

if [ -z "$current_version" ]; then
    echo "エラー: _config.ymlでバージョンが見つかりません"
    exit 1
fi

echo "現在のバージョン: $current_version"

# バージョン番号を分割
IFS='.' read -ra ADDR <<< "$current_version"
major=${ADDR[0]}
minor=${ADDR[1]}
patch=${ADDR[2]}

# バージョンアップ
case $1 in
    major)
        major=$((major + 1))
        minor=0
        patch=0
        ;;
    minor)
        minor=$((minor + 1))
        patch=0
        ;;
    patch)
        patch=$((patch + 1))
        ;;
    *)
        echo "エラー: 無効な引数です。major, minor, patch のいずれかを指定してください。"
        exit 1
        ;;
esac

new_version="$major.$minor.$patch"
echo "新しいバージョン: $new_version"

# _config.ymlを更新
sed -i "s/version: \"$current_version\"/version: \"$new_version\"/" _config.yml

# 変更をコミット
git add _config.yml
git commit -m "Bump version to $new_version

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# タグを作成
git tag -a "v$new_version" -m "Version $new_version"

echo "✅ バージョンを $current_version から $new_version に更新しました"
echo "📌 タグ v$new_version を作成しました"
echo ""
echo "次のステップ:"
echo "1. git push origin main でコミットをプッシュ"
echo "2. git push origin --tags でタグをプッシュ"