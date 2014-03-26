#!/usr/bin/python
#-*- coding: UTF-8 -*-

import web, datetime

db = web.database(dbn='sqlite', db='all.db')

def get_movies():
    return db.select('movies', order='id DESC')

def get_movie(id):
    try:
        return db.select('movies', where='id=$id order by id desc limit 100', vars=locals())[0]
    except IndexError:
        return None

def click_movie(id):
    try:
        movie = db.select('movies', where='id=$id limit 100', vars=locals())[0]
        c = movie.click_count if movie.click_count else 0
        db.update('movies', where="id=$id", vars=locals(),
                    click_count = c + 1)
        return movie.url
    except IndexError:
        return None


def new_movie(idx, title, text, url, source):
    db.insert('movies', id=idx, title=title, content=text, url=url, source=source)

def del_movie(id):
    db.delete('movies', where="id=$id", vars=locals())

def get_reviews(id):
    return db.select('reviews', where='movie=$id', vars=locals())

def new_review(movie, nick, content):
    db.insert('reviews', nick=nick, content=content, movie=movie);
    c = movie.review_count if movie.review_count else 0
    db.update('movies', where="id=$id", vars=locals(),
                review_count = c+ 1)

