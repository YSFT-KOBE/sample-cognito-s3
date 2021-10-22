# 説明
Cognito認証後にS3へファイルをアップロードするサンプルコードです。

# 使用方法
コードの以下の箇所を、適切なリソース情報に書き換えてください。

### cognito.py
* 14行目  
    ClientId='<<ユーザープールのアプリクライアントID>>'

* 33行目  
    ClientId='<<ユーザープールのアプリクライアントID>>'

* 57行目　
    IdentityPoolId='<<IDプールのID>>',

* 59行目  
    '<<Provider Names(cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID>)>>': idToken
 
* 68行目  
    '<<Provider Names(cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID>)>>': idToken

### main.py
* 19行目  
    s3client.upload('<<アップロードファイル名>>', '<<S3バケット名>>', '<<オブジェクトキー名称>>')

### s3.py
* 9行目  
    region_name='<<Region>>'
