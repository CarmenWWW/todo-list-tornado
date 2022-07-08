import tornado.web
from tornado.escape import json_encode

class ItemModel(object):

    items = {
        1: {'name': 'aaa', 'deadline': '2022-07-20'},
        2: {'name': 'bbb', 'deadline': '2022-07-10'},
    }


    @classmethod
    def get(cls, name):
        for item in cls.items.values():
            if name == (item['name']):
                return item
        return None
    
    @classmethod
    def get_all(cls):
        return list(cls.items.values())
    
    @classmethod
    def create(cls, name, deadline):
        for item in cls.items.values():
            if name == (item['name']):
                item['deadline'] = deadline
                return "item already in list, so we updated deadline"
        
        item_dict = {'name':name, 'deadline':deadline}
        max_id = max(cls.items.keys()) + 1
        cls.items[max_id] = item_dict
        return "created new item"

    
    @classmethod
    def delete(cls, name):
        for item_id in cls.items:
            if name == (cls.items[item_id]['name']):
                cls.items.pop(int(item_id))
                return "deleted"
        return "not found"




class ItemListHandler(tornado.web.RequestHandler):    
    def get(self):
        items = ItemModel.get_all()
        self.write(json_encode(items))
    
    def post(self):
        name = self.get_argument('name')
        deadline = self.get_argument('deadline')
        msg = ItemModel.create(name, deadline)
        resp = {'status': True, 'msg': msg}
        self.write(json_encode(resp))

class ItemHandler(tornado.web.RequestHandler):
    def get(self, name):
        item = ItemModel.get(name)
        if item != None:
            self.write(json_encode(item))
        else:
            return self.set_status(404)
    
    def put(self, name):
        msg = ItemModel.delete(name)
        resp = {'status': True, 'msg': msg}
        self.write(json_encode(resp))