FROM python:latest
ADD ./sillypy.py .
CMD ["python3","./sillypy.py","-h"]
