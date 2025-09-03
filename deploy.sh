#!/bin/bash
# Quick deployment script for university-chat-app

echo "🚀 University Chat App - Quick Deploy Script"
echo "============================================="

echo "📁 Current files in deployment folder:"
ls -la

echo ""
echo "🔧 Checking Git status..."
git status

echo ""
echo "📝 Next steps:"
echo "1. Push to GitHub: git add . && git commit -m 'Ready for deployment' && git push"
echo "2. Go to render.com and deploy from GitHub"
echo "3. Your app will be live in 5-10 minutes!"

echo ""
echo "🌐 Deployment platforms:"
echo "• Render: https://render.com (Recommended)"
echo "• Railway: https://railway.app"
echo "• PythonAnywhere: https://pythonanywhere.com"
