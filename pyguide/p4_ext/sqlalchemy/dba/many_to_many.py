#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.sql import select
from sqlalchemy import MetaData, Table, Column, Index, create_engine
from sqlalchemy import Integer, Float, String, MetaData, ForeignKey
import unittest

def rand_str(length):
    res = list()
    for i in range(length):
        res.append(random.choice(string.ascii_letters))
    return "".join(res)

_DB_FILE = "test.sqlite3"

class Unittest(unittest.TestCase):
    def setUp(self):
        try:
            os.remove(_DB_FILE)
        except:
            pass
        
    def test_good_way(self):
        engine = create_engine("sqlite:///%s" % _DB_FILE, echo=False)
        connect = engine.connect()
        metadata = MetaData()
        
        movie = Table("movie", metadata,
            Column("movie_id", Integer, primary_key=True),
            Column("title", String),
        )
        gener = Table("gener", metadata,
            Column("gener_id", Integer, primary_key=True),
            Column("name", String),
        )
        movie_gener = Table("movie_gener", metadata,
            Column("movie_id", Integer, ForeignKey("movie.movie_id"), primary_key=True),
            Column("gener_id", Integer, ForeignKey("gener.gener_id"), primary_key=True),
            Index("idx_movie_id", "movie_id"),
            Index("idx_gener_id", "gener_id"),
        )
        metadata.create_all(engine)
        
        # 每添加一个新movie, 删除同理
        ins = movie.insert()
        data = [{"movie_id": 1, "title": "The Shawshank Redemption"},
                {"movie_id": 2, "title": "12 Angry Men"},
                {"movie_id": 3, "title": "Schindler's List"},]
        connect.execute(ins, data)

        # 每添加一个新gener, 删除同理
        ins = gener.insert()
        data = [{"gener_id": 1, "name": "crime"},
                {"gener_id": 2, "name": "drama"},
                {"gener_id": 3, "name": "biography"},
                {"gener_id": 4, "name": "history"},]
        connect.execute(ins, data)
        
        # 每添加一个新movie_gener
        ins = movie_gener.insert()
        data = [{"movie_id": 1, "gener_id": 1},
                {"movie_id": 1, "gener_id": 2},
                {"movie_id": 2, "gener_id": 1},
                {"movie_id": 2, "gener_id": 2},
                {"movie_id": 3, "gener_id": 2},
                {"movie_id": 3, "gener_id": 3},
                {"movie_id": 3, "gener_id": 4},]
        connect.execute(ins, data)
        
        # 打印出movie_id=1的所有gener name     
        sel = select([gener.c.name]).select_from(
            gener.join(movie_gener,
                gener.c.gener_id==movie_gener.c.gener_id,                
            )
        ).where(movie_gener.c.movie_id==1)
        for row in connect.execute(sel):
            print(row.name)
        
        # 打印出gener_id=1的所有movie title
        sel = select([movie.c.title]).select_from(
            movie.join(movie_gener,
                movie.c.movie_id==movie_gener.c.movie_id,
            )
        ).where(movie_gener.c.gener_id==1)
        for row in connect.execute(sel):
            print(row.title)
            
    def tearDown(self):
        self.setUp()
        
if __name__ == "__main__":
    unittest.main()