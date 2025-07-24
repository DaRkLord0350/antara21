# build_files.sh
python -m ensurepip --upgrade
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput