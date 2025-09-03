#!/bin/bash
# Render build script to ensure no gunicorn auto-detection
echo "🔧 Building University Chat App..."
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo "✅ Build complete - will use direct Python execution"
echo "🚫 NO gunicorn workers will be used"
