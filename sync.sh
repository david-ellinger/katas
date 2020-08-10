#!/bin/bash

echo "Syncing Katas"
git pull

echo ""
echo "Staging changed files"
git add .

echo ""
echo "Committing staged files"
git commit -m "Sync Katas - $(date)"

echo ""
echo "Pushing changes to GitHub"
git push

echo ""
echo "Finished Syncing"
