import pb.auth_pb2
import pb.auth_pb2_grpc
import scripts.firestore.auth as auth
import scripts.jwt.jwt as jwt
import grpc


class AuthServer(pb.auth_pb2_grpc.AuthServiceServicer):
    # todo restrict this method by  allowing some users
    def CreateUser(self, request, context):
        auth.create_user(request.mail, request.password, request.institution, request.phone, request.name, request.surname)
        return pb.auth_pb2.Token(payload="Hello world men")

    def Login(self, request, context):
        user_claims = auth.login(request.mail, request.password)
        if user_claims is not None:
            token = jwt.generate_token(user_claims)
            return pb.auth_pb2.Token(payload=token)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details('Invalid credentials')
        return pb.auth_pb2.Token()
