ps aux | grep celery | awk '{print $2}' | xargs kill -9
celery -A pickle_tasks worker -Q pickle_queue --concurrency=2  --loglevel=info &
celery -A json_tasks worker -Q json_queue --concurrency=2 --loglevel=info &