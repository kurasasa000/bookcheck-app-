[app]
title = BookCheck
package.name = bookcheck
package.domain = org.bookcheck

source.dir = .
source.include_exts = py

version = 1.0

# 最小限の依存関係（Fire Tablet 7向け）
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Fire Tablet 7 (Fire OS 7 / Android 9)向け設定
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 28
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a

# Fire OS向け最適化
android.accept_sdk_license = True
android.skip_update = False
android.ouya.category = GAME
android.ouya.icon_filename = %(source.dir)s/data/ouya_icon.png

[buildozer]
log_level = 2
warn_on_root = 1
