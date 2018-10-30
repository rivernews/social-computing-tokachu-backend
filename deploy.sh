# ssh shaungc@104.196.204.230
# cd /var/www/html/testDjango, use port 8060

git add .
git commit -m "${1:-Fix}"
git push
eb deploy