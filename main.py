from random import randrange
from zh_wiki import zh2hant
from zh_wiki import hant2zh

def encrypt(src_bytes, mask_text, mask_offset):
    enc_uni_list=[]
    i=0
    j=mask_offset
    len_src_bytes=len(src_bytes)
    len_mask_text=len(mask_text)
    while (i//8)<len_src_bytes:
        c=mask_text[j%len_mask_text]
        if c in hant2zh:
            assert(False)
        if not (c in zh2hant):
            enc_uni_list.append(ord(c))
        else:
            byte_idx=i//8
            bit_idx=i%8
            flag=(src_bytes[byte_idx])&(0x01<<bit_idx)
            if flag:
                enc_uni_list.append(ord(zh2hant[c]))
            else:
                enc_uni_list.append(ord(c))
            i+=1
        j+=1
    encrypted_bytes=bytearray()
    for uni in enc_uni_list:
        encrypted_bytes.extend(bytes(chr(uni),'utf-8'))
    
    return encrypted_bytes

def decrypt(encrypted_text):
    src_bytes=bytearray()
    byte=0
    i=0
    for c in encrypted_text:
        if (not ((c in hant2zh) or (c in zh2hant))):
            continue
        if c in hant2zh:
            byte=byte|(0x01<<7)
        if i%8==7:
            src_bytes.append(byte)
            byte=0
        byte=byte>>1
        i+=1
    
    return src_bytes

# def main():
#     line=input('请输入需要隐写的文本(只能有一行):\n')
#     src_bytes=bytes(line, encoding='utf-8')
#     with open('sanguoyanyi.txt', encoding='utf-8') as f:
#         mask_text = f.read()
#     mask_offset=randrange(0,len(mask_text))
#     encrypted_bytes=encrypt(src_bytes,mask_text,mask_offset)

#     encrypted_text=str(encrypted_bytes, encoding='utf-8')
#     print(encrypted_text)

#     src_bytes=decrypt(encrypted_text)
#     plain_text=str(src_bytes,encoding='utf-8')
#     print(plain_text)

# if __name__=='__main__':
#     main()