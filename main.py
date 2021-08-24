from pkg_resources import resource_listdir
import cognito
import s3

print("User ID: ")
user = input()
print("Password: ")
passwd = input()

ath = cognito.CongnitoAuth()

reslt = ath.userAuthentication(user, passwd) # ユーザー認証
print(reslt)

reslt = ath.userAuthorization(reslt[2]) # ユーザー認可
print(reslt)

s3client = s3.S3(reslt[0], reslt[1], reslt[2])
s3client.upload('<<アップロードファイル名>>', '<<S3バケット名>>', '<<オブジェクトキー名称>>')
