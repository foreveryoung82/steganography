from main import decrypt 

print('从 "密文.txt" 中读取被加密的文本...')

encrypted_text=None
with open('密文.txt', 'rb') as f:
    encrypted_text=str(f.read(),'utf-8')
print('"密文.txt"读取成功!')
# print('被加密的文本是:')
# print(encrypted_text)

plain_bytes=decrypt(encrypted_text)
plain_text=str(plain_bytes, encoding='utf-8')
print()
print('成功还原隐写信息!')
print('隐写入的文本信息是:')
print(plain_text)

print()
with open('明文.txt','wb') as f:
    f.write(plain_bytes)
print('已经将上述还原出的隐写信息存入"明文.txt!"')
