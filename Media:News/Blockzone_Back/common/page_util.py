# coding=utf-8
'page util'
__author__ = 'Jiateng Liang'


class PageUtil(object):
    def __init__(self, page, page_size, max_cnt, data=None):
        self.page = page
        self.page_size = page_size
        self.max_cnt = max_cnt
        self.data = data
        self.max_page = self.get_max_page()

    def get_max_page(self):
        if self.max_cnt % self.page_size > 0:
            return (self.max_cnt / self.page_size) + 1
        elif self.max_cnt / self.page_size < 1:
            return 1
        else:
            return self.max_cnt / self.page_size

    def get_start(self):
        return (self.page - 1) * self.page_size

    def get_end(self):
        return self.page * self.page_size

    def get_show_pages(self):
        res = []
        if 1 <= self.page < 5:
            for i in range(1, min(self.max_page, 5) + 1):
                res.append(i)
            return res
        elif self.max_page >= self.page >= self.max_page - 5:
            for i in range(max(1, self.max_page - 5), self.max_page + 1):
                res.append(i)
            return res
        else:
            offset = self.page % 5
            for i in range(self.page - offset, self.page - offset + 7):
                res.append(i)
            return res
