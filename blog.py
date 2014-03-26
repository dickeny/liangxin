#!/usr/bin/python
#-*- coding: UTF-8 -*-

""" Basic blog using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/play/(\d+)', 'Play',
    '/review/(\d+)', 'Review',
)


### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)

class Play:
    def GET(self, id):
        """ View single movie """
        url = model.click_movie(int(id))
        return web.redirect(url)

class Index:
    def GET(self):
        """ Show page """
        movies = model.get_movies()
        return render.index(movies)


class View:
    def GET(self, id):
        """ View single movie """
        movie = model.get_movie(int(id))
        reviews = model.get_reviews(int(id))
        form = Review.form()
        return render.view(movie, form, reviews)


class Review:
    form = web.form.Form(
        web.form.Textbox('nick', web.form.notnull, 
            size=30,
            description=u"名称："),
        web.form.Textarea('content', web.form.notnull, 
            rows=3, cols=80,
            description="影评："),
        web.form.Button(u'发表'),
    )
    def GET(self):
        form = self.form()
        return render.review(form)

    def POST(self, id):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_review(int(id), form.d.nick, form.d.content)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
