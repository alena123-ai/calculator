[app]
title = Мой Калькулятор
package.name = mycalculator
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Зависимости (обязательно python3 и kivy)
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android специфичные настройки
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Точка входа
android.entrypoint = org.kivy.android.PythonActivity
