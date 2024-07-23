from bit import Key

# 新しいキーを生成
key = Key()

# アドレスと公開鍵、秘密鍵を表示
print("Address:", key.address)
print("Public Key:", key.public_key)
print("Private Key:", key.wif)
