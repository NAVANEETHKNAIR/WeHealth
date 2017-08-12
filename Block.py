#coding:utf-8
import hashlib
#import uuid


class Block(object):
    def __init__(self,id,value,data=None, previous_hash=None):
        #self.identifier = uuid.uuid4().hex  # 产生唯一标示
        self.identifier=int(id)
        self.value=value
        self.data = data  # 区块内容
        self.previous_hash = previous_hash# 前一个位置的hash

    def setPreHash(self,previous_hash):
        self.previous_hash = previous_hash  # 父节点哈希值

    def hash(self, nonce=None):
        '''
        计算区块的哈希值
        '''
        message = hashlib.sha256()
        message.update(str(self.identifier).encode('utf-8'))
       # message.update(str(nonce).encode('utf-8'))
        message.update(str(self.value).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()

    def get_identifier(self):
        return self.identifier
    def get_value(self):
        return self.value
    def get_data(self):
        return self.data
    def get_previoushash(self):
        return self.previous_hash
    '''
    校验区块哈希值有否有效
    def hash_is_valid(self, the_hash):

        return the_hash.startswith('0000')

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(self.nonce), self.nonce)
    '''

    '''
        新增挖矿函数
    '''
    '''
    def mine(self):
        # 初始化nonce为0
        cur_nonce = self.nonce or 0

        # 循环直到生成一个有效的哈希值
        while True:
            the_hash = self.hash(nonce=cur_nonce)
            if self.hash_is_valid(the_hash):  # 如果生成的哈希值有效
                self.nonce = cur_nonce  # 保持当前nonce值
                break  # 并退出
            else:
                cur_nonce += 1  # 若当前哈希值无效，更新nonce值，进行加1操作
    '''