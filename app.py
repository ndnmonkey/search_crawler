from flask import Flask,render_template,url_for,request
from links import get_link

app = Flask(__name__)

@app.route('/discovery/',methods=["POST","GET"])
def  discovery():
    if request.method == "GET":
        return render_template('discovery.html')
    else:
        keyword = request.form.get('key')
        page = 1  # 指的是显示第page页的信息。
        link = get_link(keyword, page)
        return render_template('discovery.html',link=link,keyword=keyword)

if __name__ == '__main__':
    app.run()
