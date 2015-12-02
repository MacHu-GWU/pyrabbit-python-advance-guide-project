#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.sql import select
from sqlalchemy import MetaData, Table, Column, Index, create_engine
from sqlalchemy import Integer, Float, String, MetaData, ForeignKey
import unittest

_DB_FILE = ":memory:"

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

        user = Table("user", metadata,
            Column("user_id", Integer, primary_key=True),
            Column("name", String),
        )
        post = Table("post", metadata,
            Column("post_id", Integer, primary_key=True),
            Column("title", String),
            Column("user_id", Integer, ForeignKey("user.user_id")),
            Index("idx_user_id", "user_id"),
        )
        metadata.create_all(engine)
        
        # 每添加一个新用户, 删除同理
        ins = user.insert()
        data = [{"user_id": 1, "name": "David"},
                {"user_id": 2, "name": "John"},
                {"user_id": 3, "name": "Mike"},]
        connect.execute(ins, data)
        
        # 每添加一个新Post, 删除同理
        ins = post.insert()
        data = [{"post_id": 1, "title": "Where to buy some fruits?", "user_id": 1},
                {"post_id": 2, "title": "Friday party recruiting!", "user_id": 1},
                {"post_id": 3, "title": "Looking for roommate.", "user_id": 2},
                {"post_id": 4, "title": "Vote me student president!", "user_id": 3},]
        connect.execute(ins, data)

        # 打印出user_id = 1的用户的所有帖子的标题
        sel = select([post.c.title]).where(post.c.user_id == 1)
        for row in connect.execute(sel):
            print(row.title)

        # 打印出post_id = 1的帖子的发帖用户的用户名
        sel = select([user.c.name]).select_from(
            user.join(post,
                user.c.user_id==post.c.user_id,
            ),
        ).where(post.c.post_id==1)
        row = connect.execute(sel).fetchone()
        print(row.name)

    def tearDown(self):
        self.setUp()
        
if __name__ == "__main__":
    unittest.main()