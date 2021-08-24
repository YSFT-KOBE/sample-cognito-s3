import boto3
import uuid


class CongnitoAuth:
    def __init__(self) :
        self.userpool_client = boto3.client('cognito-idp')
        self.idpool_client = boto3.client('cognito-identity')

    def userAuthentication(self, user, passwd, newpasswd=None): # ユーザー認証
        # ユーザーID,パスワードでの認証を実施
        response = self.userpool_client.initiate_auth(
                    AuthFlow='USER_PASSWORD_AUTH',
                    ClientId='<<ユーザープールのアプリクライアントID>>',
                    AuthParameters= {
                        "USERNAME": user,
                        "PASSWORD": passwd
                    }
        )

        chgpasswd = None
        if 'ChallengeName' in response:
            if response['ChallengeName'] == 'NEW_PASSWORD_REQUIRED': # 初回認証時のみ、パスワードの変更を求められるので、パスワード変更を実施する。
                if newpasswd == None:
                    uuidstr = str(uuid.uuid1())
                    # id = uuidstr.split('-')
                    # idnum = len(id)
                    chgpasswd = uuidstr # 新パスワードが指定されていなかった場合はUUIDを新パスワードにする。
                else:
                    chgpasswd = newpasswd
  
                response = self.userpool_client.respond_to_auth_challenge(
                            ClientId='<<ユーザープールのアプリクライアントID>>',
                            ChallengeName=response['ChallengeName'],
                            Session=response['Session'],
                            ChallengeResponses={
                                "USERNAME": user,
                                'NEW_PASSWORD': chgpasswd
                            }
                )

        accessToken =""
        refreshToken = ""
        idToken = ""
        if 'AuthenticationResult' in response :
            accessToken  = response['AuthenticationResult']['AccessToken']
            refreshToken = response['AuthenticationResult']['RefreshToken']
            idToken      = response['AuthenticationResult']['IdToken']

        if newpasswd == None:
            return accessToken, refreshToken, idToken, chgpasswd
        else:
            return accessToken, refreshToken, idToken, ""

    def userAuthorization(self, idToken): # ユーザー認可
        response = self.idpool_client.get_id(
            IdentityPoolId='<<IDプールのID>>',
            Logins={
                '<<Provider Names(cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID>)>>': idToken
            }
        )

        # print(response)

        response = self.idpool_client.get_credentials_for_identity(
            IdentityId=response['IdentityId'],
            Logins={
                '<<Provider Names(cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID>)>>': idToken
            }
        )

        # print(response)

        if 'Credentials' in response :
            accessKeyId  = response['Credentials']['AccessKeyId']
            secretKey = response['Credentials']['SecretKey']
            sessionToken = response['Credentials']['SessionToken']
            return accessKeyId, secretKey, sessionToken
        else:
            return "", "", ""
