from nerdhaus import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="192.168.0.165",port=9002)
