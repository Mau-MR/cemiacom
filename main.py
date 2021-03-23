import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import pb.auth_pb2_grpc as auth_service
import pb.auth_pb2 as auth
import scripts.auth.auth_server as  auth_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_service.add_AuthServiceServicer_to_server(auth_server.AuthServer(), server)
    # TODO quit reflection on production
    SERVICE_NAMES = (
        auth.DESCRIPTOR.services_by_name['AuthService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    # todo change to  parse flag of  the  port
    # todo add some logs to see  the status of the server
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

def main():
    serve()


if __name__ == '__main__':
    main()
