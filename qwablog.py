from flask import Flask, render_template
import codecs
import markdown
import glob
import os

app = Flask(__name__)

@app.route("/")
def hello():
    md_files =  glob.glob(os.getcwd() + "/posts/*.md")
    html_posts = []

    for md_file in sorted(md_files, reverse=True):
        input_file = codecs.open(md_file, mode="r", encoding="utf-8")
        text = input_file.read()
        html_posts.append(markdown.markdown(text,['codehilite']))

    return render_template('entries.html', posts=html_posts)

if __name__ == "__main__":
    app.debug = False
    app.run()
