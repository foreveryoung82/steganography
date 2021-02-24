from random import randrange
from main import encrypt 

print('从 "明文.txt" 中读取需要加密的文本...')

plain_text=None
with open('明文.txt') as f:
    plain_text=f.read()
print('"明文.txt"读取成功!')
# print('需要加密的文本是:')
# print(plain_text)

with open('sanguoyanyi.txt', encoding='utf-8') as f:
    mask_text = f.read()
mask_offset=randrange(0,len(mask_text))
src_bytes=bytes(plain_text, 'utf-8')
encrypted_bytes=encrypt(src_bytes,mask_text,mask_offset)

print()
print('加密后的文本是:')
encrypted_text=str(encrypted_bytes, encoding='utf-8')
print(encrypted_text)

print()
with open('密文.txt','wb') as f:
    f.write(encrypted_bytes)
print('已经将上述加密文本存入"密文.txt!"')
