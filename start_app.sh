#!/bin/bash
echo "🚀 CUSTOM STARTUP: University Chat App"
echo "🔧 Using Python directly - NO gunicorn detection"
export PYTHONUNBUFFERED=1
exec python main.py
