CREATE TABLE movies (
    id integer primary key AUTOINCREMENT,
    url TEXT,
    title TEXT,
    source TEXT,
    content TEXT,
    click_count integer DEFAULT 0,
    review_count integer DEFAULT 0,
    create_time DATETIME DEFAULT (datetime('now','localtime'))
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nick TEXT,
    content TEXT,
    movie INTEGER,
    create_time DATETIME DEFAULT (datetime('now','localtime')),
    FOREIGN KEY(movie) REFERENCES movies(id)
);

