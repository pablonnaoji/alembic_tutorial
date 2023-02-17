echo "Checking to see if we can migrate"

if [ -d "/alembic" ] 
then
    "alembic upgrade head"
else
    echo "alembic not found"
fi

echo "Check finished"

exec "$@"