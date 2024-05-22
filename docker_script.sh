docker build -t sl_map_test .

docker run -p 8501:8501 --rm -it -v /Users/kjoshi/PycharmProjects/sl_map_test:/sl_map_test sl_map_test bash