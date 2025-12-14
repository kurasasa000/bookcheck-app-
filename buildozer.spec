[app]
title = BookCheck
package.name = bookcheck
package.domain = org.bookcheck

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
