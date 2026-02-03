@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================
echo YouTube 字幕提取工具 - 测试脚本
echo ========================================
echo.

REM 设置 Python 路径
set PYTHON=C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\python.exe
set SCRIPT_DIR=%~dp0

echo 使用 Python: %PYTHON%
echo 脚本目录: %SCRIPT_DIR%
echo.

REM 测试 1: 显示帮助
echo ========================================
echo 测试 1: 显示帮助信息
echo ========================================
"%PYTHON%" "%SCRIPT_DIR%youtube_subtitle_extractor.py" --help
echo.

REM 测试 2: 单个视频提取 - 纯文本
echo ========================================
echo 测试 2: 单个视频提取（纯文本）
echo ========================================
"%PYTHON%" "%SCRIPT_DIR%youtube_subtitle_extractor.py" https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
echo.

REM 测试 3: 单个视频提取 - SRT 格式
echo ========================================
echo 测试 3: 单个视频提取（SRT 格式）
echo ========================================
"%PYTHON%" "%SCRIPT_DIR%youtube_subtitle_extractor.py" https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output "%SCRIPT_DIR%test_output.srt"
echo.

REM 测试 4: 批量提取
echo ========================================
echo 测试 4: 批量提取
echo ========================================
"%PYTHON%" "%SCRIPT_DIR%batch_extract.py" "%SCRIPT_DIR%url.txt" --output-dir "%SCRIPT_DIR%subtitles"
echo.

echo ========================================
echo 所有测试完成！
echo ========================================
echo.
echo 查看输出文件:
echo - test_output.srt
echo - subtitles/ 目录
echo.

pause
